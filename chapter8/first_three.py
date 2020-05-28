def display_message():
    return "Om Aim Hreem Shreem Kleem Sree Matre Namaha"

def favorite_book(title):
    return f"One of my favorite books is {title.title()}"

def make_shirt(size="large", message="I love Python"):
    return f"{size.title()} T-Shirt has {message.title()} on it"

def describe_city(name, country="England"):
    return f"{name.title()} is in {country.title()}"

def city_country(city, country):
    return f"{city.title()}, {country.title()}"


def make_album(name, title, num=None):
    album = {
        "name" : name.title(),
        "title" : title.title()
    }
    if num != None:
        album["songs"] = num
    return album