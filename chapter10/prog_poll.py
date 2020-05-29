def prog_poll(filename):
    with open (filename, 'w') as writer:
        while True:
            response = input("Why do you like programming, enter 'q' to exit: ")
            if response == 'q':
                break
            writer.write(f"{response}\n")


prog_poll("responses.txt")