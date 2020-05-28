flag = True
while flag:
    age =input("Enter your age or enter quit? ")
    if age == "quit":
        flag = False
    else:
        age = int(age) 
        if (age < 3):
            print("Ticket is free")
        elif (age >= 3 and age < 12):
            print("Tickt cost is $10") 
        elif (age >= 12):
            print("Ticket cost is $15")


print("Using break statement")
while True:
    age =input("Enter your age or enter quit? ")
    if age == "quit":
        break
    else:
        age = int(age) 
        if (age < 3):
            print("Ticket is free")
        elif (age >= 3 and age < 12):
            print("Tickt cost is $10") 
        elif (age >= 12):
            print("Ticket cost is $15")


"""
print("Infinite Loop")
i = 0 
while True:
    print("num", i)           
    i += 1
"""    