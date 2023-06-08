# Определить, является ли год високосным.
year = int(input('Введите год: '))
if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print(f'{year} год  обычный')
else:
    print(f'{year} год високосный')