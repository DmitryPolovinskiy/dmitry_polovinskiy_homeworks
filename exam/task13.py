# Дан список чисел, необходимо удалить все вхождения числа 20 из него.
list1 = [i for i in range(1,29)]
for i in list1:
    if i == 20:
        list1.remove(i)
        print(list1)