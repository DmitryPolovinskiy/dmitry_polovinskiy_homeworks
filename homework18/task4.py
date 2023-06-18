# Функция для определения всех чисел, на которые без остатка делится указанное.

def number(num1):
    list_of_numbers = []
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            list_of_numbers.append(i)
    return list_of_numbers


input_num = int(input('Введите число: '))
print(number(input_num))