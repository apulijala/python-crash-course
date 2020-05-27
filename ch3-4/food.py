my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are: ")
for food in my_foods:
    print(food)


print("\nMy Friedn's favorite foods are: ")
for food in friend_foods:
    print(food)

print("\nAdding different  food items to food and friend food")
my_foods.append("Cannoli")
print("\nNew My foods are: ")
for food in my_foods:
    print(food)


print("\nNew My Friend's foods are: ")
friend_foods.append("Ice Cream")
for food in friend_foods:
    print(food)


print("\nUsing Shallow Copy")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

print("My favorite foods are: ")
for food in my_foods:
    print(food)


print("\nMy Friedn's favorite foods are: ")
for food in friend_foods:
    print(food)

my_foods.append("Cannoli")
friend_foods.append("Ice Cream")
print("After apeending different foods are : ")

print("\nMy favorite foods are: ")
for food in my_foods:
    print(food)

print("\nMy Friedn's favorite foods are: ")
for food in friend_foods:
    print(food)
