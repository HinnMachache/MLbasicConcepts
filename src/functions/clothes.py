from src.classes.clothing import Clothing, Shirt, Pants, Blouse

clothing = Clothing('orange', 'M', 'stripes', 35)
blouse = Blouse('blue', 'M', 'luxury', 40, 'Brazil')
pants = Pants('black', 32, 'baggy', 60, 30)
shirt = Shirt('Black', 'L', 'Luxury', 45, 'Short')

print(f"{clothing.__class__} : {clothing.__dict__}")
print(f"{blouse.__class__} : {blouse.__dict__}")
print(f"{pants.__class__} : {pants.__dict__}")
print(f"{shirt.__class__} : {shirt.__dict__}")

shirt.change_price(56)
print(f"{shirt.__class__} : {shirt.__dict__}")




