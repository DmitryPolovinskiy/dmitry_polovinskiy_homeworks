# Придумать свою задачу на тему занятия. Обязательно использовать несколько вложений else elif if.
# Доказать что данная фигура является квадратом.
AB = int(input('Введите первую сторону: '))
BC = int(input('Введите вторую сторону: '))
CD = int(input('Введите третью сторону: '))
DA = int(input('Введите четвертую сторону: '))
AC = int(input('Введите первую диагональ: '))
BD = int(input('Введите вторую диагональ: '))
cornA = int(input('Введите угол A: '))
cornB = int(input('Введите угол B: '))
cornC = int(input('Введите угол C: '))
cornD = int(input('Введите угол D: '))
if AB == BC == CD == DA and AC == BD:
    print(f'Данна фигура является квадратом')
elif cornA == cornB == cornC == cornD == 90:
    print(f'Данная фигура является квадратом')
else:
    print(f'Данная фигура не является квадратом')