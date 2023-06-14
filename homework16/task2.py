# Создайте программу, которая, принимая массив имён, возвращает строку описывающая количество лайков (как в
# Facebook). Примеры: likes() -> "no one likes this" likes("Ann") -> "Ann likes this" likes("Ann", "Alex") -> "Ann
# and Alex like this" likes("Ann", "Alex", "Mark") -> "Ann, Alex and Mark like this" likes("Ann", "Alex", "Mark",
# "Max") -> "Ann, Alex and 2 others like this"
def likes(names):
    like = len(names)
    if like == 0:
        return 'no one likes this'
    elif like == 1:
        return names[0] + ' likes this'
    elif 1 < like <= 3:
        return ' and '.join(names) + ' like this'
    else:
        return ', '.join(names[0:2]) + f' and {str(like-2)} others like this'


print(likes([]))
print(likes(['Ann']))
print(likes(['Ann', 'Alex']))
print(likes(['Ann', 'Alex', 'Mark']))
print(likes(['Ann', 'Alex', 'Mark', 'Max', 'John']))