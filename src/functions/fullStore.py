from src.classes.pants import Pants
from src.classes.salesPerson import SalesPerson

pants = Pants('red', 35, 36, 15.12)
# print(f"Color: {pants.color}\nWaist size: {pants.waist_size}\nLength: {pants.length}\nPrice: {pants.price}")
pants.change_price(10)
# print(f"New Price: {pants.price}")
discount = pants.discount(.1)
# print(f"Discount: {discount}")

pants_one = Pants('red', 35, 36, 15.12)
pants_two = Pants('blue', 40, 38, 24.12)
pants_three = Pants('tan', 28, 30, 8.12)
salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)

print(f"First name: {salesperson.first_name}")
print(f"Last name: {salesperson.last_name}")
print(f"Employee ID: {salesperson.employee_id}")
print(f"Salary: {salesperson.salary}")
print(f"Pants sold: {salesperson.pants_sold}")
print(f"Total sales: {salesperson.total_sales}")
