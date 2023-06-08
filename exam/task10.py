# Вывести на экран числа от 0 до 50, кроме 35.
list1 = [i for i in range(0, 51)]
for i in list1:
    if i == 35:
        continue
    print(i)