
def persons_quote(famous_person, quote):
    message = f"{famous_person.title()} once said, {quote}"
    return message

"""
    Removes the white space from the name of the person. 
    It can be new line, 
    tab separated 
"""
def strip_white_space(name):
    return name.strip()

# This is the favorite number
def favorite_number(number):
    return f"My Favorite number is {number}"