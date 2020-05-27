current_users = ["andrew", "prasanna", "prasad", "arvind", "rama"]
new_users = ["john", "andrew", "datta", "digambara", "lalitha", "prasad"]

for user in new_users:
    if user in current_users:
        print(f"{user} has been used")
    else:
        print(f"{user} is available")


numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th
        ")
        
