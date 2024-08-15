# Pants class\n",
# "\n",
# "Write a Pants class with the following characteristics:\n",
# "* the class name should be Pants\n",
# "* the class attributes should include\n",
# " * color\n",
# " * waist_size\n",
# " * length\n",
# " * price\n",
# "* the class should have an init function that initializes all of the attributes\n",
# "* the class should have two methods\n",
# " * change_price() a method to change the price attribute\n",
# " * discount() to calculate a discount"


class Pants:
    """
    Pants class to represent a blue print of pants sold in a store
    """

    def __init__(self, color, waist_size, length, price):
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    # @property
    # def price(self):
    #     return self._price

    # @price.setter
    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)
