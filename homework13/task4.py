# Имеется файл file.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту:
# •	количество букв латинского алфавита;
# •	число слов;
# •	число строк.
# Пример ввода и вывода
# Предположим, что file.txt содержит приведенный ниже текст:
with open('file1.txt', 'w') as file:
    file.write("Beautiful is better than ugly.\n"
               "Explicit is better than implicit.\n"
               "Simple is better than complex.\n"
               "Complex is better than complicated.")
letters = 0
words = 0
lines = 0
with open('file1.txt', 'r') as file:
    text = file.readlines()
    for elem in text:
        words += len(elem.split())
        letters += sum(map(str.isalpha, elem))
        lines += 1
print(f'Статистика по тексту: \n{letters} букв латинского алфавита \n{words} слов\n{lines} строки ')
