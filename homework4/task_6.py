# Заполнить список степенями числа 2 (от 2^1 до 2^n) ( не самим создать такой список, а сделать так чтобы ваша
# программа сгенерировала сама такой список.
num1 = 2
num2 = 1
num3 = int(input("Введите степень: "))
list1 = (i for i in range(num2, num3))
list2 = [num1 ** i for i in list1]
print(f'Новый список: {list2}')