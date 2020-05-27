

def places_to_visit():
    locations = ["Varanasi", "Kedarnath", "Badrinath", "Dwaraka", "Ukraine"]
    print(f"Places to visit")
    print(locations)

def places_to_visit_using_sorted():
    locations = ["Varanasi", "Kedarnath", "Badrinath", "Dwaraka", "Ukraine"]
    print("\nSorted Locations")
    print(sorted(locations))
    print("\n Original List")
    print(locations)

def places_to_visit_reversed():
    locations = ["Varanasi", "Kedarnath", "Badrinath", "Dwaraka", "Ukraine"]
    print("\n places to visit")
    print("Original List")
    print(locations)
    print("Reversed Locations")
    locations.reverse()
    print(locations)
    print("Reversed again List")
    locations.reverse()
    print(locations)


def places_to_visit_using_sort():
    locations = ["Varanasi", "Kedarnath", "Badrinath", "Dwaraka", "Ukraine"]
    print("\nSorted Locations using sort")
    locations.sort()
    print(locations)
    print("\n Rerversed List")
    locations.sort(reverse=True)
    print(locations)
