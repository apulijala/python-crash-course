vacations = {}
while True:
    name = input("Enter your name or enter quit? ")
    if name == "quit":
        break
    vacation = input("If you could visit one place in the world, where would you go? ")
    vacations[name] = vacation


print("\nResults of the Poll \n")
for user, vacation in vacations.items():
    print(f"{user.title()} likes to visit {vacation.title()}")