import json
import os.path as path

"""
Stores the user and favorite number in a file called filename. 
if filename does not exist, assume it is first time and 
still store the user
"""
def store_fav_num(filename, user, num):
    users = {}
    try:
        with open(filename) as file_obj:
            users = json.load(file_obj)
            users[user] = num
    except FileNotFoundError: 
        users[user] = num # first_time no problem
    
    with open(filename, 'w') as writer:
        json.dump(users,writer)
    
def get_fav_num(filename, user):
    try:
        with open(filename) as obj:
            users = json.load(obj)
            if user in users.keys():
                return users[user]
            else:
                return None
            return users[user]
            
    except FileNotFoundError as e:
        print(f"{e.filename} not found" )
        return None
        
filename = "users.json"
while True:
    name = input("Enter user name or 'q' to exit: ")
    if name == "q":
        break
    favnum = get_fav_num(filename, name)
    if favnum != None:
        print(f"{name}, your favorite number is {favnum}")
    else:
        number = input(f"{name}, Please enter your favorite number: ")
        store_fav_num(filename,name, number )