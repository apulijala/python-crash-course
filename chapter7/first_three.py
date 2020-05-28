def rental_car():
    car = input("What kind of car do you like? ")
    print(f"Let me see if I can find you a {car.title()}")


def restaurant(num):
    if num > 8:
        return "You'll have to wait for the table"
    else: 
        return "Table is ready"


def multiples_of_ten(num):
    return num % 10 == 0