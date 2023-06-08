#Вычислить сумму цифр случайного трёхзначного числа
import random
number = random.randint(10, 99)
print(number)
f_number = number // 10
s_number = number % 10
result = (f_number + s_number )
print(result)