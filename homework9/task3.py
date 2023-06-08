# Задан список слов, в которых встречается символ ‘_’  подчеркивание). Создать новый список, в котором символ
# подчеркивания в словах ‘_’ заменить символом ‘ ‘ (пробел). l = [ "ab_cd_e", "abc", "a_b_c", "a__bc_d_", "__" ]
list1 = ["ab_cd_e", "abc", "a_b_c", "a__bc_d_", "__"]
newlist = []
sign = "_"
space = " "
for words in list1:
    if sign in words:
        word = words.replace(sign, space)
        newlist.append(word)
    else:
        newlist.append(words)
print(newlist)