# Есть список состоящий из слов и чисел, нужно записать в файл сначала слова в порядке их длины, а после слов
# цифры в порядке возрастания.
list1 = ['bird', 289, 14, 23, 'hello', 'homework']
list_of_words = []
list_of_numbers = []
with open('new_file.txt', 'a') as file:
    for elements in list1:
        if str(elements).isalpha():
            list_of_words.append(elements)
            list_of_words.sort(key=len)
        elif str(elements).isdigit():
            list_of_numbers.append(elements)
            list_of_numbers.sort()
    file.write(f'{list_of_words}\n{list_of_numbers}')