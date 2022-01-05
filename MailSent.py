import smtplib
from email.mime.text import MIMEText
import time

'''account = 'b10717029@yuntech.edu.tw'
password = 'yucheng0934'
smtp = smtplib.SMTP('webmail.yuntech.edu.tw', 25)
smtp.ehlo()
#smtp.starttls() >> yuntech webmail doesn't support
smtp.login(account, password)'''

class mail:
    def __init__(self, account, password):
        self.account = account
        self.password = password
        self.smtp = smtplib.SMTP('webmail.yuntech.edu.tw', 25)

    def connect(self):
        self.smtp.ehlo()
        try:
            result = self.smtp.login(self.account, self.password)
            '''
            type of result is 'tuple'
            if login success >> result[0] is 235
            '''
            return result
        except smtplib.SMTPRecipientsRefused as e:
            return e

    def sent(self, from_addr, to_addr, subject, msg):
        try:
            msg = MIMEText(msg)
            msg['Subject'] = subject
            msg['From'] = from_addr
            msg['To'] = to_addr
            result = self.smtp.send_message(msg)
            return result
        except smtplib.SMTPRecipientsRefused as e:
            return e

'''def mail_sent(account, password, from_addr, to_addr, subject, msg):
    try:
        msg = MIMEText(msg)
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_addr
        smtp = smtplib.SMTP('webmail.yuntech.edu.tw', 25)
        smtp.ehlo()
        #smtp.starttls() >> yuntech webmail doesn't support
        smtp.login(account, password)
        result = smtp.send_message(msg)
        return result
    except smtplib.SMTPRecipientsRefused as e:
        return e'''


'''test = mail('b10717029@yuntech.edu.tw', 'yucheng0934')
tacc = test.account
tpass = test.password
result = test.connect()
start = time.time()
sent = test.sent('b10717029@yuntech.edu.tw', 'b10717029@yuntech.edu.tw', 'class test', 'success')
end = time.time()
use = round(end - start, 3)
print('acc:{}\npass:{}\nresult:{}\nuse:{}s'.format(tacc, tpass, result, use))
print(type(result))
print(result[0])'''