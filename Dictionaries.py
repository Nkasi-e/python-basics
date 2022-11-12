# Dictionaries allows us to store key value pairs, it's a data structure

person = {
    "name": "Nkasi",
    "class": "2022",
    "age": 4
}

# METHODS IN DICTIONARY
# Note: Dictionaries also has methods like List

print(person["name"], person["age"])  # How to access a specific key
print(person.keys())  # Getting the keys in the dictionary
print(person.values())  # Getting the values in the dictionary
print(person.get("class"))  # another method to access specific key in dict
person["name"] = "Emmanuel"  # Updating a key in a dict
print(person)
person.clear()  # For clearing dictionary
