##Stings
# name = "NaDZz Leonaldson"
# name2 = "Jinxon"
# name3 = "Yes Sulek"
# name4 = "Joya"
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Strings with indexes
# names = [
#     "NaDZz Leonaldson", #0
#     "Jinxon", #1
#     "Yes Sulek", #2
#     "Joya", #3
# ]

# print(names[3]) 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Interger List
# numbers = [100, 200, 300, 400, 500]

# print(numbers[4])
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Mixed List
# mixed = [100, "NaDZz Leonaldson", 200, "Jinxon", 300, "Yes Sulek", 400, "Joya", 500]

# print(mixed[8])
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Modifying List
# names = ["banana", "apple", "microsoft"]

# names[1] = "cherry"

# print(names)
#result ['banana', 'cherry', 'microsoft'] because of the 2nd value
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Adding to a List
# names = ["banana", "apple", "microsoft"]

# names.append("cherry")

# print(names)
#REsult ['banana', 'apple', 'microsoft', 'cherry'] because of the append value
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##removing from a List
# names = ["banana", "apple", "microsoft"]

# names.remove("apple")

# print(names)
#Result ['banana', 'microsoft'] because of the removed value
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##Length of a List
# names = ["banana", "apple", "microsoft"]

# print(len(names))
#Result 3 because of the length of the list it counts the number of values in the list.
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# names = ["Gene", "leonald", "Jinxon", "Sulek", "Joya"]

# for name in names:
#     print(name)
#Results it prints all the names in the list because of the for loop
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ##Exercise 1 PERFECT
# UserInput = int(input("Enter the day [1-7]: "))

# DayOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# while UserInput < 1 or UserInput > 7:
#     print("Invalid input. Please try again.")
#     UserInput = int(input("Enter the day [1-7]: "))

# print(DayOfTheWeek[UserInput - 1])
#Results it prints the day of the week based on the user input
#Results it prints the day of the week based on the user input and command line
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ##Exercise 2 PERFECT

# ShapesNames = ["Triangle", "Quadrilateral", "Pentagon", "Hexagon", "Heptagon", "Octagon", "Nonagon", "Decagon"]

# shapesInput = int(input("Enter the number of sides [3-10]: "))

# while True:
#     if shapesInput < 3 or shapesInput > 10:
#         print("Invalid input. Please try again.")
#         shapesInput = int(input("Enter the number of sides [3-10]: "))
#     else:
#         print(ShapesNames[shapesInput - 3])
#         shapesInput = int(input("Enter the number of sides [3-10]: "))
##Results has an infinite loop because of the while loop and the else statement in the code.
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercises:
# 1. Sum of List Elements:
# Write a program that calculates the sum of all elements in a list using a for loop.
# Example:

# numbers = [2, 4, 6, 8, 10]
# sum = 0 #write a program that calculates the sum of all elements in a list using a for loop
# for number in numbers:
#     sum += number  #sum = sum + number
# print(sum) #Result 30
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 2. Count Occurrences:
# Create a program that counts how many times a specific element appears in a list using a for loop.
# Example:
# Fruits = ["apple", "banana", "apple", "orange", "apple", "mango", "apple"]
# target = "apple"
# count = 0 #Create a program that counts how many times a specific element appears in a list using a for loop
# for fruit in Fruits:
#     if fruit == target:
#         count += 1
# print(count) #Result 4
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 3. Find Maximum Value:
# Develop a program that finds the maximum value in a list of numbers using a for loop.
# Example:

# numbers = [3, 7, 2, 9, 5]
# max = numbers[0] #Develop a program that finds the maximum value in a list of numbers using a for loop
# for number in numbers:
#     if number > max:
#         max = number
# print(max) #Result 9
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ##Slicing a List
# names = ["Gene", "leonald", "Jinxon", "Sulek", "Joya"]

# # anotherNmae = names.copy()

# print(names[1:4])
#Results it prints the names in the list based on the slice value
#it will only print the names from index 1 to 4 in the list it will not include the last index.
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

names = ["Gene", "leonald", "Jinxon", "Sulek", "Joya"]

print(names[:2])
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



