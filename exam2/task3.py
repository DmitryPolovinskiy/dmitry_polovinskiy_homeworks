# Создайте словарь из строки ' An apple a day keeps the doctor away' следующим образом: в качестве ключей возьмите
# символы строки, а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.
string1 = ' An apple a day keeps the doctor away'
list1 = []
for letter in string1:
    nums = string1.count(letter)
    list1.append(nums)
list2 = list(string1)
dict1 = dict(zip(list2, list1))
print(dict1)
