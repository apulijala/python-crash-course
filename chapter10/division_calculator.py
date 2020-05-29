print("Give me two numbers, and I will divide them.")
print("Enter 'q' to exit")

# Break is useful when two inputs are present.
while True:
    first_number = input("Enter First Number? ")
    if first_number == 'q':
        break
    second_number = input("Enter Second Number? ")
    if second_number == 'q':
        break
    try:
        result = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("Cannot divide by Zero")
    else:
        print(f"Result of division {result}")