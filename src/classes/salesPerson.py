class SalesPerson:
    """
    A salesperson bluePrint to represent salesperson(s) in the store
    """

    def __init__(self, first_name, last_name, employee_id, salary):
        """
        Initializes attributes with the parameters passed
        :param first_name: First name of sales person
        :param last_name: Last name of employee
        :param employee_id: Sales person employee Id
        :param salary: Sales person's salary
        """
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants: object) -> None:  #
        """
        This method receives a Pants object and appends\n",
        the object to the pants_sold attribute list\n",
        """
        self.pants_sold.append(pants)

    def display_sales(self):
        """
        Method iterates through `pants_sold` list and
        prints out the xtics of each pair of pants.
        """
        for pants in self.pants_sold:
            print(
                f"color: {pants.color}, waist_size: ${pants.waist_size}, length: {pants.length},"
                f" price: {pants.price}")

    def calculate_sales(self) -> float:
        """
        Calculates total sales for the sales person
        :return: float: total sales
        """
        for pants in self.pants_sold:
            self.total_sales += pants.price
        return self.total_sales

    def calculate_commission(self, percentage: float):
        """
        a commission based on the total sales of pants
        :param percentage: commission percentage as a decimal
        :return: total commission
        """
        sales_total = self.calculate_sales()
        total_commission = percentage * sales_total
        return total_commission
