# Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b]. Освободившиеся в конце
# массива элементы заполнить нулями.
import random


def compress_array(array1, a, b):
    i = 0
    j = 0
    while j < len(array1):
        if array1[j] < a or array1[j] > b:
            array1[i] = array1[j]
            i += 1
        j += 1
    while i < len(array1):
        array1[i] = 0
        i += 1
    return array1


a = int(input('Введите число: '))
b = int(input('Введите число: '))
array1 = [random.randint(0, 100) for i in range(a, b)]
new_array = compress_array(array1, a, b)
print(new_array)
