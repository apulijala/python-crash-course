
def string_equals(str):
    print("\n String Equals")
    if(str == "hello"):
        print(f"{str} Matched")
    else:
        print(f"{str} Not Matched")

def string_not_equals(str):
    print("\n String Not Equals")
    if (str != "hello"):
        print(f"{str} condition met")
    else: 
        print(f"{str} condition not met")


def string_equals_lower(param_string):

    print("\n string_equals_lower_case")
    if (param_string.lower() == "hello" ):
        print(f"{param_string}'s lower cases is hello" )
    else:
        print(f"{param_string}'s lower cases is not hello" )


def numerical_comparision(number):
    print("\n Numerical Comparision")
    if number == 5:
        print(f"{number} is equal to 5")
    elif number > 5:
         print(f"{number} is greater than 5")
    elif number < 5:
        print(f"{number} is less than 5")
    

def numerical_comparision_less_equals(number):
    print("\n Numerical Comparision with <=  ")
    if number <= 10:
        print(f"{number} is equal to or less than 10")
    else: 
        print(f"{number} is greater than 10")
    
def numerical_comparision_greater_equals(number):
    print("\n Numerical Comparision with >=  ")
    if number >= 11:
         print(f"{number} is greater than or equal to  11")
    else:
        print(f"{number} is less than  11")

def item_exists_in_array(number):
    print("\n item_exists_in_array")
    my_array = [2, 3, 5, 6, 7]
    if number in my_array:
        print(f"{number} exists in", my_array)
    else:
        print(f"{number} does not exist in", my_array)

def item_not_exists_in_array(number):
    print("\n item_not_exists_in_array")
    my_array = [2, 3, 5, 6, 7]
    if number not in my_array:
        print(f"{number} does not exist in", my_array)
    else:
        print(f"{number} exists in", my_array)

def or_condition(deity):
    if deity.lower() == "rama" or deity.lower() == "krishna":
        return True
    else: 
        return False

def and_condition(num):
    return num >= 5 and num <= 11