# Написать программу для вычисления значения выражений.
# Проверить правильность выполнения задания с помощью тестовых значений.
import math

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
Y = int(input('Введите третье число: '))
y = (1 / 4) * (math.sin(a + b - Y) + math.sin(b + Y - a) + math.sin(Y + a - b) - math.sin(a + b + Y))
print(y)