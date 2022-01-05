from MailProduce import mail_produce

two_class = ['11', '12', '13', '15', '21']

department_list = ['00', '11', '12', '13', '15', '16', '17', 
                    '21', '22', '23', '24', '25', '26', '28', 
                    '31', '32', '33', '35', 
                    '41', '42']

with open('mail.txt', 'w') as infile:
    for department in department_list:
        if department not in two_class:
            for i in range(1, 81):
                email = mail_produce(department, i, False)
                infile.write(email + '\n')
        else:
            for i in range(1, 81):
                email = mail_produce(department, i, False)
                infile.write(email + '\n')
            for i in range(101, 181):
                email = mail_produce(department, i, True)
                infile.write(email + '\n')