# Напишите программу, которая выполняет сравнение двух переменных.
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
if num1 > num2:
    print(f'{num1} больше чем {num2}')
elif num1 == num2:
    print(f'{num1} равно {num2}')
else:
    print(f'{num2} больше чем {num1}')