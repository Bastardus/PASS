user_pass=input('Введите пароль состоящий из букв и цифр: ')
a=1
try:
    result=a/len(user_pass)
    result = int(user_pass)
    print('пароль состоит только из цифр')
except ZeroDivisionError:
    print('Вы не ввели пароль, введите пароль!')
except:
    print('Пароль принят') 