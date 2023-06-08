# Разделить строку “Apples, Oranges, Pears, Bananas, Berries” по запятым и вывести на экран. Затем объединить
# элементы с использованием пробела, чтобы программа вывела “Apples Oranges Pears Bananas Berries”.
string = 'Apples, Oranges, Pears, Bananas, Berries'
print(f'Строка разделенная по запятым это {string.split(", ")}')
print(f'Объединенные элементы с использованием пробела это {" ".join(string.split(" "))}')
