import sqlite3
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from log_in import *
from new_test import *
from registration import *
from start import *
from student_menu import *
from tester import *


class FirstMenu(QMainWindow, Ui_start):
    def __init__(self):
        super().__init__()
        self.next_form = None
        self.setupUi(self)
        self.log_in.clicked.connect(self.log)
        self.registration.clicked.connect(self.reg)

    def log(self):
        self.next_form = LogIn()
        self.next_form.show()
        self.close()

    def reg(self):
        self.next_form = Registration()
        self.next_form.show()
        self.close()


class LogIn(QMainWindow, Ui_log_in):
    def __init__(self):
        super().__init__()
        self.new_form = None
        self.setupUi(self)
        self.log_in_button.clicked.connect(self.click)
        self.pushButton.clicked.connect(self.back)

    def back(self):
        self.new_form = FirstMenu()
        self.new_form.show()
        self.close()

    def click(self):
        login = self.login.text()
        password = self.password.text()
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        logins = cur.execute(f'''select login from user where id > 0''').fetchall()
        logins = list(map(lambda x: x[0], logins))
        passwords = cur.execute(f'''select password from user where login="{login}"''').fetchall()
        passwords = list(map(lambda x: x[0], passwords))
        if login not in logins or password not in passwords:
            self.statusbar.showMessage('Неправильный логин или пароль')
            self.login.setText('')
            self.password.setText('')
            return
        status = cur.execute(f'''select status from user where login="{login}"''').fetchall()[0][0]
        if status == 0:
            self.new_form = StudentMenu(login)
            self.new_form.show()
            self.close()
        if status == 1:
            self.new_form = NewTest(login)
            self.new_form.show()
            self.close()


class Registration(QMainWindow, Ui_Registration):
    def __init__(self):
        super().__init__()
        self.new_form = None
        self.setupUi(self)
        self.registration_button.clicked.connect(self.click)
        self.pushButton.clicked.connect(self.back)

    def back(self):
        self.new_form = FirstMenu()
        self.new_form.show()
        self.close()

    def click(self):
        if self.loginEdit.text() == '' or self.password1Edit.text() == '' \
                or self.password1Edit.text() != self.password2Edit.text():
            self.statusbar.showMessage('Неправильные данные')
            self.loginEdit.setText('')
            self.password1Edit.setText('')
            self.password2Edit.setText('')
            return
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        logins = cur.execute('''select login from user where id > 0''').fetchall()
        logins = list(map(lambda x: x[0], logins))
        if self.loginEdit.text() in logins:
            self.statusbar.showMessage('Такой логин уже существует')
            return
        n = 0
        if self.comboBox.currentText() == 'Учитель':
            n = 1
        cur.execute(f'''insert into user(login, password, status)
         values ("{self.loginEdit.text()}", "{self.password1Edit.text()}", {n})''')
        con.commit()
        self.new_form = LogIn()
        self.new_form.show()
        self.close()


class StudentMenu(QMainWindow, Ui_StudentMenu):
    def __init__(self, login):
        super().__init__()
        self.next_form = None
        self.new_form = None
        self.setupUi(self)
        self.login = login
        self.startTestButton.clicked.connect(self.click)
        self.pushButton.clicked.connect(self.back)

    def back(self):
        self.new_form = LogIn()
        self.new_form.show()
        self.close()

    def click(self):
        con = sqlite3.connect('tests.db')
        cur = con.cursor()
        keys = cur.execute('''select key from test where id > 0''').fetchall()
        keys = list(map(lambda x: x[0], keys))
        if self.codeEdit.text() not in keys:
            self.statusbar.showMessage('Ключ не действителен')
            return
        s = cur.execute(f'''select t from test where key="{self.codeEdit.text()}"''').fetchall()[0][0]
        self.next_form = Tester(s, self.login)
        self.next_form.show()
        self.close()


class NewTest(QMainWindow, Ui_NewTest):
    def __init__(self, login):
        super().__init__()
        self.answers = []
        self.login = login
        self.setupUi(self)
        self.addAnsButton.clicked.connect(self.add)
        self.cleaButton.clicked.connect(self.clear)
        self.loadButton.clicked.connect(self.load)
        self.pushButton.clicked.connect(self.back)

    def back(self):
        self.next_form = LogIn()
        self.next_form.show()
        self.close()

    def add(self):
        if self.answerEdit.text() == '' or self.qwestionEdit.text() == '':
            self.statusbar.showMessage('Некорректные данные')
            self.qwestionEdit.setText('')
            self.answerEdit.setText('')
            return
        s = self.qwestionEdit.text() + ',,,,' + self.answerEdit.text()
        self.answers.append(s)
        self.qwestionEdit.setText('')
        self.answerEdit.setText('')

    def clear(self):
        self.answerEdit.setText('')
        self.qwestionEdit.setText('')

    def load(self):
        if len(self.answers) == 0:
            self.statusbar.showMessage('Нет вопросов')
            return
        if self.codeEdit.text() == '':
            self.statusbar.showMessage('Пустое поле кода теста')
            return

        con = sqlite3.connect('tests.db')
        cur = con.cursor()
        keys = cur.execute('''select key from test where id > 0''').fetchall()
        keys = list(map(lambda x: x[0], keys))
        if self.codeEdit.text() in keys:
            self.statusbar.showMessage('Ваш ключ не уникален')
            return
        self.answers = '\n'.join(self.answers)
        cur.execute(f'''insert into test(key, t) values ("{self.codeEdit.text()}", "{self.answers}")''')
        con.commit()


class Tester(QMainWindow, Ui_Tester):
    def __init__(self, test, login):
        super().__init__()
        self.setupUi(self)
        self.login = login
        self.results = []
        # Внутри test пары вопрос ответ через \n а внутри через ,,,,
        self.test = test.split('\n')
        self.test = list(map(lambda x: x.split(',,,,'), self.test))
        self.user_answers = ['' for _ in range(len(self.test))]
        self.saveButton.clicked.connect(self.save)
        self.previewButton.clicked.connect(self.preview)
        self.nextButton.clicked.connect(self.next)
        self.endButton.clicked.connect(self.end)
        self.current_qwe = 0
        self.qwestionText.setText(self.test[self.current_qwe][0])
        self.max_qwe = len(test) - 1
        self.pushButton.clicked.connect(self.back)

    def back(self):
        self.next_form = StudentMenu(self.login)
        self.next_form.show()
        self.close()

    def save(self):
        self.user_answers[self.current_qwe] = self.answerEdit.text()

    def preview(self):
        if self.current_qwe == 0:
            self.statusbar.showMessage('Некорректный запрос')
            return
        self.current_qwe = self.current_qwe - 1
        self.qwestionText.setText(self.test[self.current_qwe][0])

    def next(self):
        if self.current_qwe + 1 > self.max_qwe:
            self.statusbar.showMessage('Некорректный запрос')
            return
        self.current_qwe = self.current_qwe + 1
        self.qwestionText.setText(self.test[self.current_qwe][0])

    def end(self):
        for i in range(self.max_qwe + 1):
            if self.user_answers[i] == self.test[i][1]:
                self.results.append(True)
            else:
                self.results.append(False)
        self.qwestionText.setText(f'Ваш результат {self.results.count(True)} из {self.max_qwe + 1}')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstMenu()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

'''Я обязательно когда-нибудь сделаю хэширование паролей'''