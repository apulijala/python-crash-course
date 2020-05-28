
sandwich_orders = ["pepperoni","pastrami",  "cheese", "egg", "pastrami", "fish", "tomato", "pastrami"]
print ("Deli has run out of Pastrami")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")


print("Removed all Pastrami sandwiches")
print(sandwich_orders)
