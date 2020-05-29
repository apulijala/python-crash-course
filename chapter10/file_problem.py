from hello_error import HelloError
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"{filename} not found")


def test_hello_not_allowed(text):
    if text == "hello":
        raise HelloError("Hello is not allowed")
    else: 
        return(f"Normal text {text}")

try:
    print(test_hello_not_allowed("hello"))
except HelloError as e:
    print(e.message)
finally: 
    print("All Done")

# Normal flow
try:
    print(test_hello_not_allowed("Jaya Guru Datta"))
except HelloError as e:
    print(e.message)
finally: 
    print("All Done")