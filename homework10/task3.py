# 3) Даны списки:
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
set1 = set(a)
set2 = set(b)
print(list(set1.intersection(set2)))
