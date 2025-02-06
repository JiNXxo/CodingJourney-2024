# DICTIONARY is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

# numbers = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5 }

# print(numbers["three"])
#Result 3 because of the key value "three"
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Days = {
#     1: "Monday",
#     2: "Tuesday",
#     3: "Wednesday",
#     4: "Thursday",
#     5: "Friday",
#     6: "Saturday",
#     7: "Sunday"
# }
# userInput = int(input("Enter a day (1-7): "))

# while userInput !=0:
#     if userInput < 1 or userInput > 7:
#         print("Invalid input. Please enter a number between 1 and 7")
#     else:
#         print(Days[userInput])
#     userInput = int(input("Enter a day (1-7): "))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Exercise: Identify the shape by its Number of Sides
#Using Dictionaries, write a python program that prompts the user to enter the number of side of a shape (an integer between 3 and 10). The program should then output the name of the corresponding polygon.

# Polygon Names by Number of Sides:
#3 Sides: Triangle
#4 Sides: Quadrilateral
#5 Sides: Pentagon
#6 Sides: Hexagon
#7 Sides: Heptagon
#8 Sides: Octagon
#9 Sides: Nonagon
#10 Sides: Decagon

# Example output
#Enter the numbe of side: 5
#A shape with 5 sides is called Pentagon

# sides = { 3: "Triangle", 4: "Quadrilateral", 5: "Pentagon", 6: "Hexagon", 7: "Heptagon", 8: "Octagon", 9: "Nonagon", 10: "Decagon" }

# userInput = int(input("Enter the number of sides: "))
# while userInput != 0:
#     if userInput < 3 or userInput > 10:
#         print("Invalid input. Please enter a number between 3 and 10")
#     else:
#         print(f"A shape with {userInput} sides is called {sides[userInput]}")
#     userInput = int(input("Enter the number of sides: "))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# #Creating a dictionary (FLAVOR)

# person = {
#     "name": "John",
#     "age": 36,
#     "height": 6.1,
#     "courses":"BSIT"
# }


# #Second way to create a dictionary (FLAVOR)
# person = dict(name="John", age=36, height=6.1, courses="BSIT")

#~~~~~~~~~~~~

# #Square brackets are used to access the value of a key in a dictionary [Recommended]

# print(person["name"])
# print(person["age"])
# print(person["height"])
# print(person["courses"])

# #.get method is used to access the value of a key in a dictionary (Recommended)

# print(person.get("name"))
# print(person.get("age"))
# print(person.get("height"))
# print(person.get("courses"))

# #accessing dictionary keys
# print(person.keys())

# #accessing dictionary values
# print(person.values())

# #accessing dictionary items
# print(person.items())

# #updating dictionary values
# person["name"] = "Jane"
# print(person)

# #Copying a dictionary
# person2 = person.copy()
# print(person2)

#Modifying a dictionary Values
# person["name"] = "Jane"
# print(person)

#Adding a new key-value pair
# person.update({"name": "Jane", "age": 26, "height": 5.6, "courses": "BSme"})
# print(person)

#Removing or Deleting a key-value pair
# del person["courses"] #(way#1)
# person.pop("courses") #(way#2)
#print(person)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#***************Looping through a dictionary******************
# for key in person:
#     print(f"{key}: {person[key]}")

# #Looping through a dictionary using .items() method
# for key, value in person.items():
#      print(f"{key}: {value}")

##Checking if a key exists in a dictionary
# if "name" in person:
#     print("Yes, 'name' is one of the keys in the person dictionary")
# else:
#     print("No, 'name' is not one of the keys in the person dictionary")

##Checking if a value exists in a dictionary
# if "Jane" in person.values():
#     print("Yes, 'Jane' is one of the values in the person dictionary")
# else:
#     print("No, 'Jane' is not one of the values in the person dictionary")

##Checking the length of a dictionary
# print(len(person))

#************Loop through dict.keys()************
##Iterating over key-value pairs
# for key, value in person.items():
#     print(f"{key}: {value}")

##Iterating over keys
# for key in person.keys():
#     print(key)

##Iterating over values 
# for value in person.values():
#     print(value)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Exercise: Create a dictionary of countries and their capitals
# country = dict(name="Philippines", population=117.3, capital="Manila", language="Filipino")
# print(f"Country: {country['name']}")
# print(f"Population: {country['population']} Million")
# print(f"Capital: {country['capital']}")
# print(f"Language: {country['language']}")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# adding a new key-value pair to a dictionary
# person = dict(name="John", age=36, height=6.1, courses="BSIT")
# person.update({"nationality": "Filipino"})

# print(person)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Exercise: Create a dictionary of countries and their capitals
#Nested Dictionaries
# import json

# Persons = {
#     "Person One": {
#         "name": "One", 
#         "age": 35, 
#         "height": 6.1, 
#         "courses": "BSIT"},
#     "Person Two": {
#         "name": "Two", 
#         "age": 36, 
#         "height": 6.2, 
#         "courses": "BSIT"},
#     "Person Three": 
#     {"name": "Three", 
#     "age": 37, 
#     "height": 6.3, 
#     "courses": "BSIT"},
#     "Person Four": {
#         "name": "Four", 
#         "age": 38, 
#         "height": 6.4, 
#         "courses": "BSIT"},
#     "Person Five": {
#         "name": "Five", 
#         "age": 38, 
#         "height": 6.5, 
#         "courses": "BSIT"},
# }

# print(json.dumps(Persons, indent=2)) #json.dumps() method converts a dictionary into a string
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
