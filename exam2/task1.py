# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt. После этого удалите созданную папку.
#  Все операции выполнять с помощью встроенных функций библиотеки os.

import os

path = "/Users/USER/DESKTOP/test_folder"

os.mkdir(path)
os.chdir("/Users/USER/DESKTOP/test_folder")
print(os.getcwd())
with open('test_1.txt', 'w+') as file:
    print(file.read())
with open('test_2.txt', 'w+') as file:
    print(file.read())
with open('test_3.txt', 'w+') as file:
    print(file.read())
os.rename('test_1.txt', 'rename_1.txt')
os.rename('test_2.txt', 'rename_2.txt')
os.rename('test_3.txt', 'rename_3.txt')
os.remove('/Users/USER/DESKTOP/test_folder/rename_1.txt')
os.remove('/Users/USER/DESKTOP/test_folder/rename_2.txt')
os.remove('/Users/USER/DESKTOP/test_folder/rename_3.txt')
os.rmdir('/Users/USER/DESKTOP/test_folder')
