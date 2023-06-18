# Написать 12 функций по переводу: 1. Дюймы в сантиметры 2. Сантиметры в дюймы 3. Мили в километры 4. Километры в
# мили 5. Фунты в килограммы 6. Килограммы в фунты 7. Унции в граммы 8. Граммы в унции 9. Галлон в литры 10. Литры в
# галлоны 11. Пинты в литры 12. Литры в пинты Написать программу, со следующим интерфейсом: пользователю
# предоставляется на выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру от одного до
# двенадцати. После программа запрашивает ввести численное значение. Затем программа выдает конвертированный
# результат. Использовать функции из первого задания. Программа должна быть в бесконечном цикле. Код выхода из
# программы - “0”.

def inches_into_cm(inches):
    return inches * 2.54


def cm_into_inches(cm):
    return cm / 2.54


def miles_into_km(miles):
    return miles * 1.60934


def km_into_miles(km):
    return km / 1.60934


def pounds_into_kg(pounds):
    return pounds * 0.453592


def kg_into_pounds(kg):
    return kg / 0.453592


def ounces_into_grams(ounces):
    return ounces * 28.3495


def grams_into_ounces(grams):
    return grams / 28.3495


def gallons_into_liters(gallons):
    return gallons * 3.78541


def liters_into_gallons(liters):
    return liters / 3.78541


def pints_into_liters(pints):
    return pints * 0.473176


def liters_into_pints(liters):
    return liters / 0.473176


while True:
    print("1. Дюймы в сантиметры")
    print("2. Сантиметры в дюймы")
    print("3. Мили в километры")
    print("4. Километры в мили")
    print("5. Фунты в килограммы")
    print("6. Килограммы в фунты")
    print("7. Унции в граммы")
    print("8. Граммы в унции")
    print("9. Галлон в литры")
    print("10. Литры в галлоны")
    print("11. Пинты в литры")
    print("12. Литры в пинты")
    print("Введите 0 для выхода из программы")
    choice = int(input("Выберите тип конвертации: "))
    if choice == 0:
        break
    value = float(input("Введите значение: "))
    if choice == 1:
        result = inches_into_cm(value)
        print(f"{value} дюймов = {result} сантиметров")
    elif choice == 2:
        result = cm_into_inches(value)
        print(f"{value} сантиметров = {result} дюймов")
    elif choice == 3:
        result = miles_into_km(value)
        print(f"{value} миль = {result} километров")
    elif choice == 4:
        result = km_into_miles(value)
        print(f"{value} километров = {result} миль")
    elif choice == 5:
        result = pounds_into_kg(value)
        print(f"{value} фунтов = {result} килограммов")
    elif choice == 6:
        result = kg_into_pounds(value)
        print(f"{value} килограммов = {result} фунтов")
    elif choice == 7:
        result = ounces_into_grams(value)
        print(f"{value} унций = {result} граммов")
    elif choice == 8:
        result = grams_into_ounces(value)
        print(f"{value} граммов = {result} унций")
    elif choice == 9:
        result = gallons_into_liters(value)
        print(f"{value} галлонов = {result} литров")
    elif choice == 10:
        result = liters_into_gallons(value)
        print(f"{value} литров = {result} галлонов")
    elif choice == 11:
        result = pints_into_liters(value)
        print(f"{value} пинт = {result} литров")
    elif choice == 12:
        result = liters_into_pints(value)
        print(f"{value} литров = {result} пинт")
    else:
        print("Неверный выбор")