
def rivers():
    river_conutries = {
        "teifi" : "wales",
        "ganga" : "india"
    }
    river_conutries["thames"] = "england"

    print("\nRiver Countries")
    for river, country in river_conutries.items():
        print(f"{river.title()} runs through {country.title()}")
    
    print("\nAll rivers are")
    for river in river_conutries.keys():
        print(f"{river.title()}")
    
    print("\nAll countries are")
    for country in river_conutries.values():
        print(f"{country.title()}")


def polling():
    favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
    
    people_list = ["rama", "jen", "krishna", "datta", "phil"]
    for person in people_list:
        if person.lower() in favorite_languages.keys():
            print(f"{person.title()}, Thanks for Responding")
        else: 
            print(f"{person.title()}, Please can you take the Poll")
