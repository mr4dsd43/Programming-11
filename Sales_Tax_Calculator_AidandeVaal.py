Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tax = 1.12
first_item = float (input ("Price of 1st item: "))
second_item = float (input("Price of second item: "))
third_item = float (input("Price of third item: "))
price = (first_item + second_item + third_item)
total = tax*price
print("Before tax: $%.2f" % price)
print("Total after tax: $%.2f" % total)
