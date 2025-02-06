# Boolean Values:
# In Python, a Boolean is a data type that can hold one of two values: True or False. 
# These values are integral to controlling the flow of a program, especially when making decisions using conditional statements.

# Creating Booleans:

# Booleans can be directly assigned:
# is_sunny = True
# is_raining = False

# They are often the result of comparison operations:
# result = 10 > 5  # result is True

# Comparison Operators:
# Comparison operators evaluate expressions and return a Boolean value:
# == : Equal to
# != : Not equal to
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to


# isPositive = True
# isNegative = False
#-------------------------------------

#-------------------------------------
# Sample of the Equal To (==)
# num = 10
# isEqualToTen = num == 10

# print(isEqualToTen)
#-------------------------------------
# Sample of the Not Equal To (!=)
# num = 9
# isNotEqualtoTen = num != 10

# print(isNotEqualtoTen)
#-------------------------------------
# Sample of Greater than 
# num = 11

# isGreaterThanTen = num > 10

# print(isGreaterThanTen)
#-------------------------------------
# Sample of Lessthan
# num = float(input("Enter a number: "))

# isLessThanTen = num < 10
# print(isLessThanTen)
#-------------------------------------
# Sample of >= : Greater than or equal to
# num = float(input("Enter a number: "))

# isGreaterThanOrEqualTo = num >= 10
# print(isGreaterThanOrEqualTo)
#-------------------------------------
# Sample of <= : Less than or equal to
# num = float(input("Enter a number: "))

# isLessThanOrEqualTo = num <= 10
# print(isLessThanOrEqualTo)
#=========================================
#TODO: Logical Operators:
# Logical operators combine Boolean values and return a Boolean result:
# and : Returns True if both operands are True
# or : Returns True if at least one operand is True
# not : Returns True if the operand is False
#   1AND                    2OR              3NOT or!
# ifItHas F auto "F"  ; ifItHas T auto "T" ;  "Irony"
# T and F = F         ; T or T = T         ; not T = F
# T and T = T         ; T or F = T         ; not F = T
# F and T = F         ; F or T = T         ;
# F and F = F         ; F or F = F         ;
#ComplexTest1
#!(T and F) or (T or F)
# "!(F)" or (T)
#T or T
#answer is "True"
#CompleTest2 "Comparison"
#!((T and F) or (T or F))
#!(F or T)
#!T
#answer is "False" 
#Note take first the parenthesis and apply the "!orNOT" in the Last Part.

#Formula for !((T and F) or (T or F))

#CT1 print(not(True and False) or (True or False))
#CT2 print(not((True and False) or (True or False)))
#=========================================
#                  Truthiness
#Truthy                               Falsy
#anything has value                 1    0      - Zero
#                                   2   None    - None
#                                   3    ""     - Empty String
#                                   4    ()     - Empty Parenthesis

# Zero and 1 is the binary 
# ZERO number is "False" and all other numbers are "true"
#print(bool(1))         = False
# print(bool(None))     = False
# print(bool())         = False
#print(bool(""))        = False
#print(bool({}))        = False
#print(bool([]))         =False
#Note:Anthing that are not on this samples are ({["TRUE"]})
#=========================================
#1 print(bool("Hello")) = True
#2 print(bool([1, 2, 3])) = True

#3 print(bool({
#     "name": "Nad Leonaldson",
#     "Age": 21
# })) = True

#4 print(bool({
    
# })) = False because it is empty
#=========================================
#age = 19
#isTicketAvailable = False
# (age >= 18) and isTicketAvailable

# age = float(input("Enter your age: "))
# hasTicket = input("Do you have a ticket? (y/n): " ).lower() == "y"

# print(age >= 18 and hasTicket)    
#=========================================

