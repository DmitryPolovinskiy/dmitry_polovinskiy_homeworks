# Есть строка со знаками препинания. Удалить из строки знаки препинания.
import re
string1 = 'Hello, my name is - Dmitry.'
new_string = re.sub(r'[^\w\s]','', string1)
print(f'Новая строка после удаления - {new_string}')