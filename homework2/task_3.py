# Ввести предложение. Если число символов в предложении кратно 3 - добавить ! к концу строки. Вывести строку на экран.
sentence = input('Введите предложение: ')
print(len(sentence))
if len(sentence) % 3 == 0:
    print(f'{sentence}!')
else:
    print(sentence)
