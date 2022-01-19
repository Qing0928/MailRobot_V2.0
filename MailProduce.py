def mail_produce(grade, department, num, two):
    if num < 10:
        email = '{}{}00{}@yuntech.edu.tw'.format(grade, department ,num)

    elif num >= 10 and two == False:
        email = '{}{}0{}@yuntech.edu.tw'.format(grade, department ,num)

    elif num >= 10 and two == True:
        email = '{}{}{}@yuntech.edu.tw'.format(grade, department ,num)
    
    return email