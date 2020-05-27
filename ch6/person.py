def person(first,last , age, city):
    person_details = {"first_name" : first.title()}
    person_details["last_name"] = last.title()
    person_details["age"] = age
    person_details["city"] = city.title()
    return person_details


def favorite_numes():
    fav_numbers = {
        "Arvind" : "8",
        "Ashwin" : 99,
        "Satya"  : 420

    }
    fav_numbers['Rao'] = 420
    fav_numbers["Datta"] = 10

    for name, num in fav_numbers.items():
        print(f"{name}'s  favroite number is {num}")

def glossary():
    print("\n Glossary terms")
    glossary_terms = {
        "for" : "For loop (for in)",
        "list" : "List of Values",
        "array" : "Declares a list ([1, 2, 3])",
        "dictionary" : "Key Value Pair",
        "if-elif-else" : "if : elif : else: "
    }
    glossary_terms["insert"] = "Insserts value in the array"
    glossary_terms["string"] = "Has title, lower and upper case"
    glossary_terms["interpreter"] = "Interprets python program"
    glossary_terms["number"] = "Reads numbers"
    glossary_terms["boolian logic"] = "use and and or not && and ||"
    glossary_terms["indent"] = "Python Works using indentation"
    
    for idiom, meaning in glossary_terms.items():
        print (f"{idiom}\n\t{meaning}")

def person_list(first,last , age, city):

    persons = []
    
    person_details = {"first_name" : first.title()}
    person_details["last_name"] = last.title()
    person_details["age"] = age
    person_details["city"] = city.title()
    persons.append(person_details)

    person_details1 = {"first_name" : "Arvind"}
    person_details1["last_name"] = "Pulijala"
    person_details1["age"] = 32
    person_details1["city"] = "London"
    persons.append(person_details1)

    person_details2 = {"first_name" : "Anna"}
    person_details2["last_name"] = "Poltova"
    person_details2["age"] = 39
    person_details2["city"] = "Ukraine"
    persons.append(person_details2)
    return persons