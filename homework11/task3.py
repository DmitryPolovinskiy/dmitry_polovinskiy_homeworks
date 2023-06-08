# В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней
# символов.
string1 = 'hello'
list1 = [1, 34, 56]
dict1 = {'a': 2, 43: 'world'}
list2 = []
number_of_lines = 0
with open('new_file3.txt', 'w') as file:
    file.write(f'{string1}\n{list1}\n{dict1}')
with open('new_file3.txt', 'r') as file:
    lines = file.readlines()
    for elem in lines:
        number_of_lines += 1
        list2.append(elem.strip())
        for i in list2:
            number_of_elements = len(i)
        print(f'Количество символов в строке - {number_of_elements}')
    print(f'Количество строк в файле - {number_of_lines}')