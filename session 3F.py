menu = {
    "chanadal": 65,
    "mongdal": 98,
    "fortune": 135,
    "gagan": 125
}

print("select the  2 items form below menu:")
print(menu)

cart = []

choice = "yes"
item1 = input("enter the item1:")
cart.append(menu[item1])

item2 = input("enter the item2:")
cart.append(menu[item2])

print("your pricing in the order")
print(cart)


"""while choice == "yes":
    item = input("enter the item:")
    cart.append(menu[item])

    choice = input("would you like to add more item (yes/no)")

print("your cart[{}]:".format(len(cart)))
print(cart)

total_amount = sum(cart)
print("total", total_amount)

promo_code = input("you any enter promo code if you have")
if promo_code == "GODFATHER":
    print("PROMO CODE APPLIED")
    total_amount = total_amount - (0.20 * total_amount)

    print("Amount After Promo Code",total_amount)

    total_amount = total_amount +(0.18 * total_amount)
    print("final amount",total_amount)"""