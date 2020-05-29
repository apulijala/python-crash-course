with open('pi_million_digits.txt') as file_obj:
    lines = file_obj.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[0:52])
print(pi_string[:52])
print(pi_string[1:52])

filename = 'programming.txt'
with open(filename, 'w') as writer:
    writer.write("this  is great\n")
    writer.write("Jaya guru datta\n")