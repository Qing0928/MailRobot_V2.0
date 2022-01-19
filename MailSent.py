import smtplib
from email.mime.text import MIMEText
import time

class mail:
    def __init__(self):
        self.smtp = smtplib.SMTP('webmail.yuntech.edu.tw', 25)

    def connect(self, account, password):
        self.smtp.ehlo()
        try:
            result = self.smtp.login(account, password)

            return result
        except smtplib.SMTPAuthenticationError as e:
            error_msg = str(e)

            return error_msg

    def sent(self, from_addr, to_addr, subject, msg):
        try:
            msg = MIMEText(msg)
            msg['Subject'] = subject
            msg['From'] = from_addr
            msg['To'] = to_addr
            result = self.smtp.send_message(msg)

            return result
        except smtplib.SMTPRecipientsRefused as e:
            error_msg = str(e)
            return error_msg
            
test = mail()
result = test.connect('b10717029@yuntech.edu.tw', 'yucheng0934')

start = time.time()
sent = test.sent('b10717029@yuntech.edu.tw', 'b10717029@yuntech.edu.tw', 'unknowtest', 'success')
print(type(sent))
sent = test.sent('b10717029@yuntech.edu.tw', 'b10717099@yuntech.edu.tw', 'unknowtest', 'success')
print(sent)
sent = test.sent('b10717029@yuntech.edu.tw', 'b10717098@yuntech.edu.tw', 'unknowtest', 'success')
print(sent)

end = time.time()
use = round(end - start, 3)

print('result:{}\nuse:{}s'.format(result, use))
