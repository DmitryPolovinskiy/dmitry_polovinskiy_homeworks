#Найти результат выражения. Переменная a вводится с клавиатуры.
a = int(input("Введите число: "))
y = (((1 + a + a ** 2) / (2 * a + a **2) + 2) - (1 - a + a ** 2) / (2 * a - a ** 2)) ** (-1) * (5 - 2 * a ** 2)
print(y)