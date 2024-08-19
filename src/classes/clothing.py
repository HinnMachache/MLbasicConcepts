class Clothing:
    """
    Clothing class, a super class which represents a cloth in a store
    """

    def __init__(self, color, size, style, price):
        """
        Initiliazes parameters to their attributes.
        :param color:
                Cloth Color
        :param size:
                Cloth size
        :param style:
                Cloth Style
        :param price:
                Cloth Price
        :return:
            None
        """
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    def change_price(self, price):
        self.price = price

    def calculate_discount(self, discount) -> float:
        """
        Find Cloth Discount
        :param discount:
                Percentage discount
        :return:
            float, discount
        """
        return self.price * (1 - discount)


class Shirt(Clothing):
    """
    Child class to Super class Clothing
    """

    def __init__(self, color, size, style, price, long_or_short):
        """
        Initializes attributes
        :param color:
                Color parameter
        :param size:
                Size Attribute
        :param style:
                Style Attribute
        :param price:
                Price attribute
        :param long_or_short:
                Long or short sleeve attribbute
        """
        # Clothing.__init__(self, color, size, style, price)
        super().__init__(color, size, style, price)
        self.long_or_short = long_or_short

    def double_price(self):
        """
        A method that doubles the shirt price
        :return:
            None
        """
        self.price = 2 * self.price


class Pants(Clothing):
    """
    Child class Pants inheriting from super class Clothing
    """

    def __init__(self, color, size, style, price, waist):
        """
        Method initializer
        :param color:
                Color Attribute
        :param size:
                Size Attribute
        :param style:
                Style Attribute
        :param price:
                Price Attribute
        :param waist:
                waist Attribute
        """
        Clothing.__init__(self, color, price, size, style)
        self.waist = waist

    def calculate_discount(self, discount) -> float:
        """
        Find Cloth Discount
        :param discount:
                Percentage discount
        :return:
            float, discount
        """
        return self.price * (1 - discount / 2)


class Blouse(Clothing):
    """
    Blouse child Class
    """

    def __init__(self, color, size, style, price, country_of_origin):
        """
        Attribute initializer
        :param color:
                Color Attribute
        :param size:
                Size Attribute
        :param style:
                Style Attribute
        :param price:
                price Attribute
        :param country_of_origin:
                Country of origin

        """
        Clothing.__init__(self, color, size, style, price)
        self.country_of_origin = country_of_origin

    def triple_price(self):
        """
        Triples price of pants
        :return:
            Flot: Trippled price
        """
        return 3 * self.price

    def calculate_shipping(self, weight, rate):
        """
        Calculate Shipping charges
        :param weight:
                Weight Attribute
        :param rate:
            Rate Attribute
        :return:
            Shipping fee
        """
        return weight * rate
