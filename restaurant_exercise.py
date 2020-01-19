brunch = {
    "Steak and Eggs": 16.99,
    "Three Egg Breakfast": 8.99,
    "Egg Benedict": 11.99,
    "Biscuit and Gravy": 7.99,
    "Chicken Fingers": 10.99,
    "Chicken Wrap": 8.99,
    "Steak Salad" : 1.99
}
drinks = {
    "Soft Drink": 1.99,
    "Coffee": 1.99,
    "Orange Juice": 0.99,
    "Milk": 0.55,
    "Water": 0.00
}

specials = {
    "Soup of the Day" : 8.99,
    "Catch of the Day" : 14.99,
    "Chef Special" : 15.99
}

brunch["Steak Salad"] = 15.99
brunch["Three Egg Breakfast"] = {
    "Without Bacon" : 8.99,
    "With Bacon" : 9.99
}

item_list = []
price_list = []

def add_item(item):
    if(item in brunch):
        item_list.append(item)
        price_list.append(brunch[item])
    elif(item in drinks):
        item_list.append(item)
        price_list.append(drinks[item])
    elif(item in specials):
        item_list.append(item)
        price_list.append(specials[item])

def print_receipt():
    count = 0
    total = 0

    while(count < len(item_list)):
        print("%s %.2f".rjust(1) % (item_list[count].ljust(35), (price_list[count])))
        count += 1
    for price in price_list:
        total += price

    taxes = (total * .07)
    suggested_tip1 = (total + taxes) * .25
    suggested_tip2 = (total + taxes) * .20
    suggested_tip3 = (total + taxes) * .15

    print("\n")
    print("Price:".rjust(37) + "  $ %s" % (total))
    print("Taxes:".rjust(37) + "  $  %.2f" % (taxes))
    print("Total:".rjust(37) + "  $ %.2f" % (total + taxes))
    print("**Suggested Tip**")
    print("Tip 25%: ".ljust(15) + "  %.2f" % (suggested_tip1))
    print("Tip 20%: ".ljust(15) + "  %.2f" % (suggested_tip2))
    print("Tip 15%: ".ljust(15) + "  %.2f" % (suggested_tip3))
        
#TABLE1
add_item("Egg Benedict")
add_item("Coffee")
add_item("Biscuit and Gravy")
add_item("Coffee")
add_item("Steak and Eggs")
add_item("Soft Drink")
print_receipt()

item_list = []
price_list = []
#TABLE2
print("")
print("")
add_item("Steak Salad")
add_item("Soft Drink")
add_item("Soup of the Day")
add_item("Chicken Wrap")
add_item("Water")
add_item("Chicken Fingers")
add_item("Soft Drink")
add_item("Chef Special")
print_receipt()
