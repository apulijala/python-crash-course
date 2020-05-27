

def guest_list():
    guests = ["Krishna", "Rama", "Govinda", "Datta"]
    print("\n")
    for guest in guests:
        print(f"Jaya Guru Datta {guest}, Please come to my Dinner")

"""
    Create a guest list minus one. 
    Removing Govinda. 
"""

def guest_list_minus_one():
    guests = ["Krishna", "Rama", "Govinda", "Datta"]
    guest_not_comming = guests.pop(2)
    print("\n")
    print("Guest List minus one")
    print(f"{guest_not_comming} has dropped out ")
    guests.insert(2, "Hari")
    for guest in guests:
        print(f"Jaya Guru Datta {guest}, Please come to my Dinner")

def add_new_guests():
    guests = ["Krishna", "Rama", "Govinda", "Datta"]
    guest_not_comming = guests.pop(2)
    print("\n")
    print("Adding New Guests")
    print(f"{guest_not_comming} has dropped out ")
    guests.insert(2, "Hari")
    guests.insert(0, "Lalitha")
    guests.insert(3, "Hanuman")
    guests.append("Lakshmi")

    for guest in guests:
        print(f"Jaya Guru Datta {guest}, Please come to my Dinner")        

def remove_all_except_two():
    guests = ["Krishna", "Rama", "Govinda", "Datta"]
    guest_not_comming = guests.pop(2)
    print("\n")
    print("Remove all except two")
    print(f"{guest_not_comming} has dropped out ")
    guests.insert(2, "Hari")
    guests.insert(0, "Lalitha")
    guests.insert(3, "Hanuman")
    guests.append("Lakshmi")
    
    print("Can invite only two people for Dinner")

    guest_removed = guests.pop()
    print(f"{guest_removed}, I cannot invite you, Sorry")
    guest_removed = guests.pop()
    print(f"{guest_removed}, I cannot invite you, Sorry")
    guest_removed = guests.pop()
    print(f"{guest_removed}, I cannot invite you, Sorry")
    guest_removed = guests.pop()
    print(f"{guest_removed}, I cannot invite you, Sorry")
    guest_removed = guests.pop()
    print(f"{guest_removed}, I cannot invite you, Sorry")
    print("\n")
    for guest in guests: 
        print(f"{guest}, You are still Invited")
    del guests[1]
    del guests[0]
    
    print("Guests now are", guests)
    