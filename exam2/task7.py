# Ввести строку. Вывести на экран букву, которая находится в середине этой строки. Также, если эта центральная
# буква равна первой букве в строке, то создать и вывести часть строки между первым и последним символами исходной
# строки. (подсказка: для получения центральной буквы, найдите длину строки и разделите ее пополам. Для создания
# результирующий строки используйте срез)
string1 = input("Введите строку: ")
len_of_string = len(string1)
mid_of_string = len_of_string // 2
print(f'Центральный символ: {string1[mid_of_string]}')
if string1[mid_of_string] == string1[0]:
    print(f"Часть строки между первым и последним символами: {string1[1:-1]}")