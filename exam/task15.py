# Необходимо удалить пустые строки из списка строк.
list1 = ['student1', '', 'student2', '', 'student3', '']
for i in list1:
    if i == '':
        list1.remove(i)
print(list1)