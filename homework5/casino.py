# Казино. Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно.
# Цифры от одного до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный,2 черный).
# Пользователю дается 5 попыток угадать номер и цвет(Прим. введения с клавиатуры: 3 красный).
# В случае неудачи вывести на экран правильную комбинацию.
import random

num1 = str(random.randint(1, 10))
num2 = str(random.randint(1, 2))
if num2 == 1:
    num2 = f'красный'
else:
    num2 = f'черный'
chance = 1
random_combination = ' '.join([num1, num2])
print(random_combination)
while chance <= 5:
    input_combination = input(f'Введите комбинацию: ')
    chance += 1
    if random_combination == input_combination:
        print(f'Вы угадали комбинацию! ')
        break
    elif chance > 5:
        print(f'Вы проиграли. Правильная комбинация - {random_combination}')
    else:
        print(f'Вы не угадали. Попробуйте еще раз.')
