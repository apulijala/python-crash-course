contents = ''
with open ('pi_digits.txt') as my_file:
    # contents = my_file.read()
    contents = my_file.readlines()

print(f"--{contents}--")
# print(f"--{contents.rstrip()}--")

pi_string = ''
for line in contents: # You can treat string as an array of characters
    pi_string += line.rstrip()

print(pi_string)


with open ('pi_digits.txt') as my_file:
    for line in my_file:
        print(line.rstrip())

