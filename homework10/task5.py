# 5) Создайте 2 множества:
#   Если они одинаковые: вывести что они равны
#   Если 1 множество полностью состоит из второго:
#   вывести сообщение множество 1 состоит из множества 2
#   Если 2 множество полностью состоит из 1:
#   вывести сообщение множество 2 состоит из множества 1
#   Если они пересекаются: вывести элементы в которых они пересекаются
#   Если не пересекаются: вывести сообщение об этом
set1 = {1, 23, 45, 90, 'sun'}
set2 = {14, 2, 'table', 34}
if set1 == set2:
    print(f'множество 1 равно множеству 2')
elif set1.issubset(set2):
    print(f'1 множество полностью состоит из 2 множества')
elif set2.issubset(set1):
    print(f'2 множество полностью состоит из 1 множества')
elif set1.intersection(set2):
    print(f'2 множества пересекаются в элементе{set1.intersection(set2)}')
elif set1.isdisjoint(set2):
    print(f'Множества не пересекаются')

