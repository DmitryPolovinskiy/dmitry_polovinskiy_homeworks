# Есть строка ‘Привет, это пример строки в алфавитном порядке', необходимо вывести на экран слова в алфавитном порядке
string1 = 'Привет, это пример строки в алфавитном порядке'
string2 = string1.lower()
list1 = list(string2.split(' '))
list1.sort()
print(list1)