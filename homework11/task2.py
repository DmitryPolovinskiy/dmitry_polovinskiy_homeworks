# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.
with open('new_file2.txt', 'a') as file:
    while True:
        string1 = input(f'Введите данные:\n')
        file.write(f'{string1}\n')
        if string1 == '':
            break
