
def stages_of_life(age):
    if age < 2:
        return "baby"
    elif age >= 2 and age < 4:
        return "toddler"
    elif age >= 4 and age < 13:
        return "kid"
    elif age >= 13 and age < 20:
        return "teenager"
    elif age >= 20 and age < 65:
        return "adult"
    elif age >= 65:
        return "elder"

def favorite_fruits(fruit):
    fav_fruits = ["oranges", "bananas", "grapes"]
    return fruit.lower() in fav_fruits
    