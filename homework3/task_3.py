# Дана следующая функция y = f(x)
x = int(input('Введите число: '))
y = 2 * x - 10
y1 = 0
y2 = 2 * abs(x) - 1
if x > 0:
    print(y)
elif x == 0:
    print(y1)
else:
    print(y2)


