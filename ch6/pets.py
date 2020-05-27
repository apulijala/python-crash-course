def pets():
    pets = []
    pet = {
        "owner" : "Andrew Hughes",
        "type" : "Dog"
    }
    pets.append(pet)
    pet1 = {
        "owner" : "Arvind Pulijala",
        "type" : "Horse"
    }
    pets.append(pet1)
    pet2 = {
        "owner" : "Datta Digambara",
        "type" : "Dog"
    }
    pets.append(pet2)
    pet3 = {
        "owner" : "Swamiji",
        "type" : "Parrot"
    }
    pets.append(pet3)
    print("\n")
    for pet in pets:
        print(f"Pet's owner is {pet['owner']}")
        print(f"Pet is {pet['type']}")


def favorite_places():
    favorite_places = {
        "Arvind" : ["LLandysul", "London", "Mysore"],
        "Rama" : ["Ayodhya", "Varanasi", "mithila"],
        "krishna" : ["mathura", "brindavan", "vaikuntha"],
        "datta" : ["mysore", "himalayas", "vindhya", "pithapuram"]
    }

    for name, fav_places in favorite_places.items():
        print(f"{name.title()}'s favorite places are as follows: ")
        for fav_place in fav_places:
            print(f"\t{fav_place.title()}")

def cities_info():
    cities = {
        "london" : {
            "population" : "8.92 Million",
            "country" : "uk",
            "fact" : "capital of uk"
        },

        "varanasi" : {
            "population" : "1.202 million",
            "country" : "india",
            "fact" : "abode of shiva"
        }, 

        "new york" : {
            "population" : "8.399 million",
            "country" : "United States",
            "fact" : "the largest city in the United States."
        }, 

        "milan" : {
            "population" : "1.352 million",
            "country" : "italy",
            "fact" : "The Last Supper is present"
        }

    }

    for city, detail in cities.items():
        print(f"{city.title()}'s details: ")
        print(f"{city.title()} is in {detail['country'].title()}")
        print(f"{city.title()} population is {detail['population']}")
        print(f"{detail['fact'].title()}", "\n")

    