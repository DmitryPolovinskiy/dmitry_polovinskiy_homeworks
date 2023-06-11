# 2) Если в функцию передается кортеж, то посчитать длину всех его слов. Если список, то посчитать кол-во букв и
# чисел в нем. Число - количество нечетных цифр. Строка - количество букв.


def function(x):
    if type(x) == tuple:
        return sum([len(i) for i in x])
    elif type(x) == list:
        sum_let = len([str(i) for i in ("".join(map(str, x))) if i.isalpha()])
        digit_sum = len([i for i in x if str(i).isdigit()])
        # Если нужно посчитать количество цифр
        # digit_sum = len([int(i) for i in ("".join(map(str, x))) if i.isdigit()])
        return sum_let, digit_sum
    elif type(x) == int:
        nums1 = []
        for digits in str(x):
            if (int(digits) % 2) != 0:
                nums1.append(digits)
        nums2 = len(nums1)
        return nums2
    elif type(x) == str:
        len_of_string = len(x) - x.count(' ')
        return len_of_string


tuple1 = ('hello world', 'name')
list1 = ['my name', 12, 124324, 'hi']
nums = 3274593845
string1 = 'Hello world'
print(f'Длинна всех слов кортежа равна - {function(tuple1)}')
print(f'Количество букв и чисел в списке - {function(list1)}')
print(f'Количество нечетных цифр - {function(nums)}')
print(f'Количество букв в строке - {function(string1)}')
