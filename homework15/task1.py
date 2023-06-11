# 1) Простейший калькулятор c введёнными двумя числами вещественного типа. Ввод с клавиатуры: операции + - * / и
# два числа. Операции являются функциями. Обработать ошибку: “Деление на ноль” Ноль использовать в качестве
# завершения программы (сделать как отдельную операцию).
def calculator():
    num1 = float(input("Введите первое число: "))
    num2 = float(input('Введите второе число: '))
    sign = input('Выберите операцию: ')
    result1 = num1 + num2
    result2 = num1 - num2
    result4 = num1 * num2
    if sign == '+':
        print(result1)
    elif sign == '-':
        print(result2)
    elif sign == '*':
        print(result4)
    elif sign == '/':
        try:
            result3 = num1 / num2
            print(result3)
        except ZeroDivisionError:
            print('На ноль делить нельзя')
    else:
        print('Error')


calculator()
