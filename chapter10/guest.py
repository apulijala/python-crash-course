def guest(filename):
     with open(filename, 'w') as writer:
        while True:
            name = input("Enter your name or press 'q' to exit? ")
            if (name == 'q'):
                break
            writer.write(f"{name}\n")
            writer.flush()


guest("guests.txt")