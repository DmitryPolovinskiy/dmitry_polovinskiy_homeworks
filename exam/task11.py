# Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”]. В новый список добавить элементы,
# которые содержат пробел.
string1 = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
new_list = [list1 for list1 in string1 if " " in list1]
print(new_list)