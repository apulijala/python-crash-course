
def pizzas():
    pizzas = ("Pepperoni", "Cheese", "Tomato")
    print("\n")
    for pizza in pizzas:
        print(f"I like {pizza}")
    print("I really love Pizza!")

def pets():
    pets = ("Dog", "Horse", "Cat")
    print("\n")
    for pet in pets:
        print(f"A {pet} would make a great Pet")
    print("Any of these animals would make a great pet!")


def counting_to_twenty():
    for number in range(1,21):
        print(number)

def million_nums():
    million = list(range(1,1000001))
    print("Sum of million numbers is ", sum(million))
    print("Minimum of million numbers is ", min(million))
    print("Maximum of million nummbers is", max(million))

def threes():
    list_of_threes = [value*3 for value in range(1,11)]
    print("\nList of threes are")
    for num in list_of_threes:
        print(num)

def cubes_using_for_loop():
    nums_1_to_10 = list(range(1, 11))
    print("\n Cubes Using for loop")
    for num in nums_1_to_10:
        print(num**3)

def cubes_using_for_comprehension():
    print("\n Cubes Using for comprehension")
    cubes_1_to_10 = [value**3 for value in list(range(1, 11))] 
    for num in cubes_1_to_10:
        print(num)
    
    print("\n First three items")
    print(cubes_1_to_10[0:3])
    print("\n Middle three items")
    print(cubes_1_to_10[3:6])
    print("\n Last three items")
    print(cubes_1_to_10[7:])

def pizzas_deep_copy():
    pizzas = ["Pepperoni", "Cheese", "Tomato"]
    friend_pizzas = pizzas[:]
    friend_pizzas.append("Green Chillies")
    pizzas.append("Marmelade")

    print("\n Original Pizzas are")
    for orig_pizza in pizzas:
        print(f"Original pizza is {orig_pizza}")

    print("\n Friend Pizzas are")
    for friend_pizza in friend_pizzas:
        print(f"Friend pizza is {friend_pizza}")

