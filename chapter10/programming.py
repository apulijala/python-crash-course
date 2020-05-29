print(100/0)

try:
    print(100/0)
except ZeroDivisionError:
    print("Cannot divide by Zero")