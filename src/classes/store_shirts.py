class Shirts:
    """
    A Shirt Class to represents shirts in a store
    """
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.__price = shirt_price # 'Private' attribute. Name has been tangled

    @property   # Getter
    def price(self):
        return self.__price

    @price.setter   # Setter
    def price(self, new_price):
        if new_price < 40:
            new_price = 40
        self.__price = new_price

    def discount(self, discount):
        return self.__price * (1 - discount)
