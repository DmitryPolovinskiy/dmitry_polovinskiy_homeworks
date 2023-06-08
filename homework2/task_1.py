# Дана строка.

string = input('Введите строку: ')
# Сначала выведите третий символ этой строки.
print(f'Третий символ строки это {string[2]}')

# Во второй строке выведите предпоследний символ этой строки.
print(f'Последний символ строки это {string[-2]}')

# В третьей строке выведите первые пять символов этой строки.
print(f'Первые пять символов строки это {string[:5]}')

# В четвертой строке выведите всю строку, кроме последних двух символов.
print(f'Строка без двух последних символов это {string[:-2]}')

# В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы
# выводятся начиная с первого).
print(f'Четные символы строки это {string[::2]}')

# В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
print(f'Нечетные символы строки это {string[1::2]}')

# В седьмой строке выведите все символы в обратном порядке.
print(f'Строка в обратном порядке это {string[::-1]}')

# В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
print(f'Строка в обратном порядке через один символ это {string[::-2]}')

# В девятой строке выведите длину данной строки.
print(f'Длина строки = {len(string)}')
