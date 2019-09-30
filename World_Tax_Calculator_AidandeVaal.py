tax1 = 1.05
tax2 = 1.13
tax3 = 1.11
total = float( input("Please enter your total price: "))
country = input ("Please enter your country: ")
if country == "Canada" :
    province = input("Please enter your province: ")

if country == "USA" :
    print ("You don't have any tax")
    totalprice = total
    print ("Total cost is %.2f dollars" % totalprice)

if country == "Russia" :
    print ("You don't have any tax")
    totalprice = total
    print ("Total cost is %.2f dollars" % totalprice)

if country == "China" :
    print ("You don't have any tax")
    totalprice = total
    print ("Total cost is %.2f dollars" % totalprice)

if country == "Europe" :
    print ("You don't have any tax")
    totalprice = total
    print ("Total cost is %.2f dollars" % totalprice)

if country == "Australia" :
    print ("You don't have any tax")
    totalprice = total
    print ("Total cost is %.2f dollars" % totalprice)

if country == "Africa" :
    print ("You don't have any tax")
    totalprice = total
    print ("Total cost is %.2f dollars" % totalprice)

if province == "Alberta" :
    totalprice = total*tax1
    print(totalprice)
    print ("Total cost is %.2f dollars" % totalprice)

if province == "Ontario" \
   or province == "New Brunswick" or province == "Nova Scotia" :
    totalprice = total*tax2
    print(totalprice)
    print ("Total cost is %.2f dollars" % totalprice)

if province == "British Columbia" or province == "Saskatchewan" \
   or province == "Manitoba" or province == "Quebec" \
   or province == "Prince Edward Island" or province == "Newfoundland and Labrador" \
   or province == "Nunavut" or province == "Yukon" \
   or province == "Northwest Territories" :
    totalprice = total*tax3
    print ("Total cost is %.2f dollars" % totalprice)
time.sleep(10)
