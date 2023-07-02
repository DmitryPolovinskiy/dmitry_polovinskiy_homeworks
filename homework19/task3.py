class Soda:
    def __init__(self, addition=None):
        self.addition = addition

    def show_my_drink(self):
        if self.addition:
            print(f"Газировка и {self.addition}")
        else:
            print("Обычная газировка")


soda1 = Soda()
soda1.show_my_drink()

soda2 = Soda("апельсин")
soda2.show_my_drink()
