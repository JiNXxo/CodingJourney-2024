##Sample#1
# for character in "Hello World":
#     print(character)

#=================================================================
##Sample#2
# for character in "banana":
#     print(character)
#=================================================================
# character = input("input a character: ")

# if (character == "b" or
#     character == "a" or
#     character == "n" or
#     character == "a" or
#     character == "n" or
#     character == "a"):
#     print(f"{character} is a vowel")
# else:
#     print(f"{character} is a consonant")
#=================================================================

# for character in "banana":
#     if character == "a":
#         print(f"{character} is a vowel")
#     else:
#         print(f"{character} is a consonant")

#=================================================================
# for character in "saging":
#     if character == "a"or character == "e" or character == "i" or character == "o" or character == "u":
#         print(f"{character} is a vowel")
#     else:
#         print(f"{character} is a consonant")

#=================================================================
# userinput = input("Enter a word: ")

# for character in userinput:
#     if character == "a"or character == "e" or character == "i" or character == "o" or character == "u":
#         print(f"{character} is a vowel")
#     else:
#         print(f"{character} is a consonant")
#=================================================================
#Write a program that separetes even and ood numbers from a list into two different lists.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)  
print(even)
print(odd)
#=================================================================
##Filter Possitive Numbers
# Write a program that iterates through a list of integers and creates a new list containing only the positive numbers.
numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
positive = []

for number in numbers:
    if number > 0:
        positive.append(number)

print(positive)
#=================================================================