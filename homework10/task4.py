# Дана строка. Сохранить в ней только первые вхождения символов, удалив все остальные. Результат вывести в виде кортежа.
string1 = 'My name is'
print(set(string1))
print(tuple(set(string1).pop()))