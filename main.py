import sys
import time
from MailProduce import mail_produce
from MailSent import mail
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from UI import Ui_Form
from LoginUI import Ui_Form as Login_Form

two_class = ['11', '12', '13', '15', '21']

department_list = ['00', '11', '12', '13', '15', '16', '17', 
                    '21', '22', '23', '24', '25', '26', '28', 
                    '31', '32', '33', '35', 
                    '41', '42']
grade = ''
auto_mail = mail()
account = ''

class SentMailThread(QThread):
    trigger = pyqtSignal(str)
    finished = pyqtSignal()
    def __init__(self, subject, msg):
        super().__init__()
        self.subject = subject
        self.msg = msg

    def run(self):
        for department in department_list:
            if department not in two_class:
                for i in range(1, 81):
                    email = mail_produce(grade, department, i, False)
                    result = auto_mail.sent(account, email, self.subject, self.msg)
                    if result == {}:
                        self.trigger.emit(email)
                    elif '550' in result:
                        self.trigger.emit('fail:{}'.format(result))
                        break
                    time.sleep(0.1)
                    
            else:
                for i in range(1, 81):
                    email = mail_produce(grade, department, i, False)
                    result = auto_mail.sent(account, email, self.subject, self.msg)
                    if result == {}:
                        self.trigger.emit(email)
                    elif '550' in result:
                        self.trigger.emit('fail:{}'.format(result))
                        break
                    time.sleep(0.1)
                    
                for i in range(101, 181):
                    email = mail_produce(grade, department, i, True)
                    result = auto_mail.sent(account, email, self.subject, self.msg)
                    if result == {}:
                        self.trigger.emit(email)
                    elif '550' in result:
                        self.trigger.emit('fail:{}'.format(result))
                        break
                    time.sleep(0.1)
                    
                    
        self.finished.emit()

class Body(QMainWindow):
    def __init__(self):
        global account, password
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.sentButton.clicked.connect(self.sentbtn)

    def sentbtn(self): 
        mail_subject = self.ui.subject.toPlainText()
        mail_body = self.ui.body.toPlainText()
        global grade
        grade = self.ui.password_2.toPlainText()
        if grade == '':
            error_msg = QMessageBox()
            error_msg.setWindowTitle('錯誤訊息')
            error_msg.setText('學號前四碼未輸入')
            error_msg.setStandardButtons(QMessageBox.Ok)
            reaction = error_msg.exec()
            error_msg.show()

        if mail_body != '' and mail_subject != '' and grade != '':
            self.work = SentMailThread(mail_subject, mail_body)
            self.work.start()
            self.ui.sentButton.setDisabled(True)
            self.work.trigger.connect(self.UpdateBroswer)
            self.work.finished.connect(self.ThreadFinish)
        else:
            error_msg = QMessageBox()
            error_msg.setWindowTitle('錯誤訊息')
            error_msg.setText('主旨與信件內容不可空白')
            error_msg.setStandardButtons(QMessageBox.Ok)
            reaction = error_msg.exec()
            if reaction == QMessageBox.Ok:
                pass
            error_msg.show()

    def UpdateBroswer(self, text):
        self.ui.body_2.append(text)

    def ThreadFinish(self):
        self.ui.sentButton.setDisabled(False)

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Login_Form()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.login_btn)

    def login_btn(self):
        global account
        account = self.ui.accountEdit.toPlainText()
        password = self.ui.passwordEdit.toPlainText()

        if (account == '') or (password == ''):
            account = '123'
            password = '123'
        
        login_result = auto_mail.connect(account, password)
        
        if login_result == '(504, b\'Authentication failed.\')':
            account = ''
            password = ''
            error_msg = QMessageBox()
            error_msg.setWindowTitle('登入結果')
            error_msg.setText('登入失敗')
            error_msg.setStandardButtons(QMessageBox.Ok)
            reaction = error_msg.exec()
            if reaction == QMessageBox.Ok:
                pass
            else:
                pass
            error_msg.show()

        else:
            error_msg = QMessageBox()
            error_msg.setWindowTitle('登入結果')
            error_msg.setText('登入成功')
            error_msg.setStandardButtons(QMessageBox.Ok)
            reaction = error_msg.exec()
            if reaction == QMessageBox.Ok:
                window_login.destroy()
                window_main.ui.nowaccount.setText(account)
                window_main.show()
            else:
                pass
            error_msg.show()

qApp = QApplication(sys.argv)
window_main = Body()
window_login = Login()
window_login.show()
sys.exit(qApp.exec())