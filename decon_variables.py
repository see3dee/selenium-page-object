# Destructure Dictionary:
people = {"Bob": 34, "Jane": 56, "Greg": 45}

print(f"use list(Dict.items) to get this: {list(people.items())}")  # a list of tuples for each dict element
print(f"use Dict.keys to get this: {people.keys()}")  # a list of strings
print(f"use Dict.values to get this: {people.values()}")  # a list of values

for person, age in people.items():
    print(f"{person} is {age}")

# Destructure a list of tuples
car_best_years = [("Buick", "Skylark", 1972, "blue"), ("Chevorlet", "Malibu", 2010, "Red"),
                  ("Toyota", "Celica", 1972, "MAC Truck Blue")]

# Ignoring any elements of a broken out variable
for make, model, year, _ in car_best_years:
    print(f"{make} made the {model} in the year: {year}")

