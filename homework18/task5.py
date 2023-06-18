# Функция для определения того, является ли строка палиндромом
def palindrom(str1):
    if str1 == str1[::-1]:
        return f'Строка {str1} является палиндромом.'
    else:
        return f'Данная строка не является палиндромом.'


input_string = input('Введите строку: ')
print(palindrom(input_string))
