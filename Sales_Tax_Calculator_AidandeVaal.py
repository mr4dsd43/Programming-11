
tax = 1.12
first_item = float (input ("Price of 1st item: "))
second_item = float (input("Price of second item: "))
third_item = float (input("Price of third item: "))
price = (first_item + second_item + third_item)
total = tax*price
print("Before tax: $%.2f" % price)
print("Total after tax: $%.2f" % total)
