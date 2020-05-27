
def city_country(city, county, population = ''):
    if population != '':
        city_county1 = f"{city}, {county} - population {population}"
    else:
        city_county1 = f"{city}, {county}"
        
    return city_county1.title()