def cats_and_dogs(cats_file, dogs_file):
    
    print("All Cats")
    try:
        with open(cats_file) as catfile:
            cats = catfile.readlines()
            for cat in cats:
                print(cat.rstrip())
    except FileNotFoundError as fe:
        print(f"{fe.filename} not found")

        print("\nAll Dogs")
    try:    
        with open(dogs_file) as dogfile:
            dogs = dogfile.readlines()
            for dog in dogs:
                print(dog.rstrip())
    except FileNotFoundError as fe:
        print(f"{fe.filename} not found")
        
cats_and_dogs("cats.txt", "dogs1.txt")