import json
users = {
    "Andrew" : {
        "food" : ["pizza", "cake", "pastry", "hello"], 
        "last_name" : "Hughes", 
        "skills" : ["Gardening"],
        "Teacher" : "Arvind K. Pulijala"
    },
    "Arvind" : {
        "food" : ["Aloo", "Mutton", "Rose", "Lily"], 
        "last_name" : "Pulijala", 
        "skills" : ["Java", "Python", "AWS", "Docker", "Kubernetes"], 
        "Teacher" : "Bill White"
    }
}

filename = "users.json"
with open(filename, "w") as f:
    json.dump(users, f)


with open(filename) as f:
    users_read = json.load(f)

print("users read are")
print(users_read)
print(f'User Third Skill is {users_read["Arvind"]["skills"][2]}' )