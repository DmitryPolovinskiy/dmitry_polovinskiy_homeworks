# Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем
# календаре, и False иначе.

def date(day, month, year):
    if month < 1 or month > 12:
        return 'Данной даты не существет'
    if day < 1:
        return 'Данной даты не существет'
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day > 29:
                return 'Данной даты не существет'
        elif day > 28:
            return 'Данной даты не существет'
    elif month in [4, 6, 9, 11]:
        if day > 30:
            return 'Данной даты не существет'
    else:
        if day > 31:
            return 'Данной даты не существет'
    return f'{day}.{month}.{year} - Данная дата существует'


input_day = int(input('Введите день: '))
input_month = int(input('Введите месяц: '))
input_year = int(input('Введите год: '))
print(date(input_day, input_month, input_year))