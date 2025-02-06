##  "IF"
# num = -1

# if (num > 0):
#     print(f"{num} is a positive number.") 
    # Anything below Zero has no result because of the condition.
#----------------------------------------------------------------
## "IF + ELSE"
# num = -1

# if (num > 0):
#     print(f"{num} is a positive number.")     
# else:
#     print(f"{num} is a negative number.")
#----------------------------------------------------------------
## "IF + ELIF + ELSE"
# num = 0

# if (num > 0):
#     print(f"{num} is a positive number.") 
# elif (num < 0):
#     print(f"{num} is a negative number.")    
# else:
#     print(f"{num} is zero.")

#=================================================================
#Activity #1
# age = int(input("Enter your age: "))

# if (age > 0 and age <= 12):
#     print("You are a child.")
# elif (age >= 13 and age <= 19):
#     print("You are a Teenager")
# elif (age >= 20 and age <= 64):
#     print("You are an Adult")
# else:
#     print("You are a Senior")
# #=================================================================
# day = int(input("Enter the day: "))


# if (day == 1):
#     print("Monday")
# elif (day == 2):
#     print("Tuesday")
# elif (day == 3):
#     print("wednesday")
# elif (day == 4):
#     print("thursday")
# elif (day == 5):
#     print("friday")
# elif (day == 6):
#     print("saturday")
# elif (day == 7):
#     print("sunday")
# else:
#     print("Invalid Number")
# #=================================================================
# grade = int(input("Enter the Grade: "))
            
# if (grade >= 90 and grade <= 100):
#     print("A")
# elif (grade >= 80 and grade <= 89):
#     print("B")
# elif (grade >= 70 and grade <= 79):
#     print("C")
# elif (grade >= 60 and grade <= 69):
#     print("D")
# elif (grade <= 59):
#     print("F")
# else:
#     print("Invalid Number")
# #=================================================================
##Number Comparison
# Ask the user for two numbers
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter Second number: "))

# if num1 > num2:
#     print("num1 is greater than num2")
# elif num2 > num1:
#     print("num2 is greater than num1")
# else:
#     print("num1 us equal to num2")
# #=================================================================
# sides = int(input("Enter the number of sides: "))

# if (sides == 3):
#     print("Triangle")
# elif (sides == 4):
#     print("Quadrilateral")
# elif (sides == 5):
#     print("Pentagon")
# elif (sides == 6):
#     print("Hexagon")
# elif (sides == 7):
#     print("Heptagon")
# elif (sides == 8):
#     print("Octagon")
# elif (sides == 9):
#     print("Nonagon")
# elif (sides == 10):
#     print("Decagon")
# else:
#     print("Invalid Number")
# #=================================================================
# character = input("Enter a single letter: ")

# if len(character) != 1 or not character.isalpha():
#     print("Invalid input. Please enter a single alphabetical letter.")
# else:

#     if character in 'aeiou' :
#         print(f"{character} is a vowel.")
#     else:
#         print(f"{character} is a consonant. ")
# #=================================================================
character = input("input a character: ")

if (character == 'a' or
    character == 'e' or
    character == 'i' or
    character == 'o' or
    character == 'u'):
    print(f"{character} is a vowel.")
else:
    print(f"{character} is a consonant.")
