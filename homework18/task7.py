# Напишите функцию, которая определяет количество гласных в строке
def find_vowels(sentence):
    vowels = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
    counter_vowels = 0
    for i in sentence:
        if i in vowels:
            counter_vowels += 1
    return f'Количество гласных в строке - {counter_vowels}'


str1 = input('Введите строку: ')
print(find_vowels(str1))