item1=input("What is the price of your 1st item? $")
item2=input("What is the price of your 2nd item? $")
total = int(item1) + int(item2)
if float(total) > 49:
    print int(total)
else:
    added = int(total) + 10
    print int(added)
        

            
