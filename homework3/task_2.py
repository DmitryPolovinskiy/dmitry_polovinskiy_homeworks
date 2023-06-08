# Определить существование треугольника.
# 1 первый метод
side1 = float(input("Введите первую сторону: "))
side2 = float(input("Введите вторую сторону: "))
side3 = float(input("Введите третью сторону: "))
if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
    print(f'Треуголник существует')
else:
    print(f'Треугольник не существует')

# 2 метод
corner1 = int(input('Введите первый угол: '))
corner2 = int(input("Введите второй угол: "))
corner3 = int(input('Введите третий угол: '))
if corner1 + corner2 + corner3 == 180:
    print(f"Треугольник существует")
else:
    print(f'Треугольник не существует')
