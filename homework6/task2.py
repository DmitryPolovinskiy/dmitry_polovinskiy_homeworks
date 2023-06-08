# Даны 2 списка: a = [4,6,'pу','tell',78] b = [44,'hello’,56,'exept’,3] Выполнить следующие операции: 1)Сложить
# два списка 2) Добавьте элемент 6 на 3 позицию. 3)Удалите все текстовые переменные 4) Посчитайте количество
# элементов списка
list1 = [4, 6, 'pу', 'tell', 78]
list2 = [44, 'hello', 56, 'exept', 3]
list3 = list1 + list2
list3.insert(3, 6)
print(list3)
for text in list3:
    if type(text) == str:
        list3.remove(text)
print(list3)
print(len(list3))