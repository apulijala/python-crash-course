def add():
    while True:
        num1 = input("Enter first number or q to exit:  ")
        if num1 == "q":
            break
        try: 
            num1 = int(num1)
        except ValueError:
            print("num1 cannot be a string. Please enter number")
            continue

        num2 = input("Enter Second number or q to exit:  ")
        if num2 == "q":
            break
        try: 
            num2 = int(num2)
        except ValueError:
            print("num2 cannot be a string. Please enter number")
            continue

        result = num1 + num2
        print(f"result of adding {num1} and {num2} is {result}")


add()