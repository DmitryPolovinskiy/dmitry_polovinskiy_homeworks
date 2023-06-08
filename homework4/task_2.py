# Есть список с четными и нечетными элементами. Посчитать количество четных и нечетных элементов.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
chetnye = 0
nechetnye = 0
for i in list1:
    if i % 2 != 0:
        nechetnye += 1
    else:
        chetnye += 1
print(f'Четных элементов - {chetnye}')
print(f'Нечетных элементов - {nechetnye}')
