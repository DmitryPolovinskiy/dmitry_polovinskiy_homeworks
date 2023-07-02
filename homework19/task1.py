class Calculator:
    def __init__(self, num1_str, num2_str):
        self.num1_str = num1_str
        self.num2_str = num2_str
        self.num1_valid, self.num1 = self.validator(num1_str)
        self.num2_valid, self.num2 = self.validator(num2_str)

    def validator(self, num_str):
        try:
            num = float(num_str)
            return True, num
        except ValueError:
            return False, None

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            raise ValueError("На ноль делить нельзя")
        return self.num1 / self.num2

    def calculate(self, operation):
        if not self.num1_valid or not self.num2_valid:
            raise ValueError("Неправильный ввод\nВведите число")

        if operation == "Сложение":
            return self.add()
        elif operation == "Вычитание":
            return self.subtract()
        elif operation == "Умножение":
            return self.multiply()
        elif operation == "Деление":
            return self.divide()
        else:
            raise ValueError("Неверная операция")


def main():
    num1_str = input("Введите первую цифру: ")
    num2_str = input("Введите вторую цифру: ")
    calc = Calculator(num1_str, num2_str)

    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    operation = input("Введите номер (1-4): ")

    try:
        if operation == "1":
            result = calc.calculate("Сложение")
        elif operation == "2":
            result = calc.calculate("Вычитание")
        elif operation == "3":
            result = calc.calculate("Умножение")
        elif operation == "4":
            result = calc.calculate("Деление")
        else:
            raise ValueError("Неверный выбор\nВведите число от 1 до 4")
        print(f"Результат: {result}")
    except ValueError as e:
        print(e)


main()
