usernames = ["admin", "rama", "krishna", "datta", "lalitha"]
usernames = []
if usernames: 
    for user in usernames:
        if user.lower() == "admin":
            print(f"Hello {user}, would you like to see a status report? ")
        else: 
            print(f"Hello {user}, thanks for logging in again ")
else:
    print("You need to find users")