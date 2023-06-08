# Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин)
# в введенной строке (программа не должна зависеть от регистра вводимых символов).
# Например, в строке "acggtgttat" процентное содержание
# символов G и C равно 4/10 ⋅ 100 = 40.0 где 4 - это количество символов G и C, а 10 -- это длина строки.
str1 = str(input('Введите символы: '))
new_str = str1.lower()
len_str = len(new_str)
c = 0
g = 0
for i in new_str:
    if i == "c":
        c += 1
    elif i == "g":
        g += 1
percent = (c + g) / len_str * 100
print(f'Процент гуанина и цитозина в строке - {percent} процента')