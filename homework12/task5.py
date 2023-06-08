# Сгенерировать список используя генератор списков. В списке должно быть 10 элементов в произвольном случайном
# диапазоне. Перевести все числа в строку и получить из списка -  строку.
import random
list1 = [random.randint(0, 100) for i in range(10)]
print(' '.join(str(num) for num in list1))

# 2 способ
# string1 = ''
# for num in list1:
#     string1 += str(num)
#     string1 += ' '
# print(string1)
