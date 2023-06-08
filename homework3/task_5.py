# Пользователь вводит три числа. Если все числа больше 10, то вывести yes, иначе no.
num1 = float(input('Введите любое число: '))
num2 = float(input('Введите любое число: '))
num3 = float(input('Введите любое число: '))
if num1 > 10 and num2 > 10 and num3 > 10:
    print('yes')
else:
    print('no')