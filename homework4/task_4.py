# Дан список чисел. Если число встречается более двух раз, то добавить его в новый список.
list1 = [1, 2, 3, 4, 1, 1, 3, 4, 5, 6, 3, 4]
print(f'Список чисел : {list1}')
list2 = []
for i in list1:
    if list1.count(i) > 2:
        list2.append(i)
        if list2.count(i) > 1:
                list2.remove(i)
print(f'Новый список : {list2}')

# list1 = [1, 2, 3, 4, 1, 1, 3, 4, 5, 6, 3, 4]
# list2 = []
# list2.append(1)
# list2.append(3)
# list2.append(4)
# print(list2)