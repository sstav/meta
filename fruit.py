# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class AppleBasket:
    def __init__(self, color, amount):
        self.color_apple = color
        self.quantity_apple = amount

    def increase(self):
        self.quantity_apple = self.quantity_apple + 1

    def __str__(self):
        return "A basket of " + str(self.quantity_apple) + " " + str(self.color_apple) + "apples."


# OpenU - Maman 13 - Question 2.A
if __name__ == '__main__':
    InstA = AppleBasket("red", 4)
    InstB = AppleBasket("blue", 50)

    FruitBasket = [InstA,InstB]
    for fruit in FruitBasket:
        print(fruit)




