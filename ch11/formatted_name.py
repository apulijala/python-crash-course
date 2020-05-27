def get_formatted_name(first, last, middle = ''):

    if middle != '':
        full_name = f"{first} {middle} {last}"
    else: 
        full_name = f"{first} {last}"
    return full_name.title()


"""
result = get_formatted_name("arvind", "pulijala")
print(result)
"""
print("Enter q at any time to quit")

"""
while True: 
    first = input("Enter the First Name? ")
    if first == 'q':
        break
    last = input("Enter the Last Name? ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"Formatted name is {formatted_name}")
"""