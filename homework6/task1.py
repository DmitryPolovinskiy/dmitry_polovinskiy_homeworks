# Дан список list=[15,48,'hello',6,19,'world’]. Все числа этого списка проверить на чётность. Если число чётное,
# то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке. Все слова: посчитать количество гласных
# и согласных. Вывести всё на экран.
list1 = [15, 48, 'hello', 6, 19, 'world']
list2 = []
for digit in list1:
    if type(digit) == int:
        if digit % 2 == 0:
            num1 = digit % 10
            num2 = digit // 10
            num3 = num1 + num2
            list2.append(num3)
        else:
            ind = list1.index(digit)
            list1[ind] = 1

print(f'Сумма чисел четных чисел :{list2}')
print(f'Список с замененными нечетными числами: {list1}')
listofwords = []
vowels = ['e', 'o']
vowel = 0
consonant = 0
for words in list1:
    if type(words) == str:
        listofwords.append(words)
words = ''.join(listofwords)
for let in words:
    if let in vowels:
        vowel += 1
    else:
        consonant += 1
print(f'Количество гласных - {vowel}')
print(f'Количество согласных - {consonant}')



