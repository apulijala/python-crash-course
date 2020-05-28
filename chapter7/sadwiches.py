
sandwich_orders = ["pepperoni","pastrami",  "cheese", "egg", "pastrami", "fish", "tomato", "pastrami"]
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwhich")
    finished_sandwiches.append(sandwich)

print("\n")
print("\n\nAll sandwiches are made\n")

for sandwich in finished_sandwiches:
    print(f"{sandwich} was made and finshed")

