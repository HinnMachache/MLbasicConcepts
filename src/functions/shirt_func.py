from src.classes.store_shirts import Shirts

shirt_one = Shirts("blue", "S", "Short_sleeve", 32)
shirt_two = Shirts("black", "L", "Short_sleeve", 34)
shirt_three = Shirts("Red", "M", "Long_sleeve", 35)

# shirt_three.__price = 45
new_price = shirt_two.price
shirt_two.price = 30
newest_price = shirt_two.price

print(new_price)
print(newest_price)

shirt_list = []
shirt_list.append(shirt_one)
shirt_list.append(shirt_two)
shirt_list.append(shirt_three)

for i in range(len(shirt_list)):
    print(shirt_list[i].__dict__)


# doc = shirt_three.__repr__()
# print(doc)
