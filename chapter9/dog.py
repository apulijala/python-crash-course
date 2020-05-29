class Dog():
    def __init__(self, name):
        self.name = name 
    
    def bark(self):
        print(f"{self.name} is barking")

    def rollover(self):
        self.bark()
        print(f"{self.name} rollover")


dog = Dog("Arnab")
dog.rollover()