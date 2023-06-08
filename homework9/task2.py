# Создайте словарь d = {'1': 0, ‘2’: 0, '3': 0} тремя способами. Выведите полученный словарь на экран

dictionary1 = {'1': 0, '2': 0, '3': 0}
print(dictionary1)
dictionary2 = dict.fromkeys(['1', '2', '3'], 0)
print(dictionary2)
dictionary3 = {str(i): 0 for i in range(1, 4)}
print(dictionary3)