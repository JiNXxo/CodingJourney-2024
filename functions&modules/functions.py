# def add(x, y):
#     # print("The value of x is: " + str(x))
#     # print("The value of y is: " + str(y))
#     print("The sum of x and y is: " + str(x + y))

# add(10, 20)
# add(30, 40)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# create functions add, subtract, divide, multiply *LOGICAL ERROR*
# def add(x, y):
#     sub = x - y
#     divide = x / y
#     multiply = x * y

#     print("The value of x is: " + str(x))
#     print("The value of y is: " + str(y))
#     print("The sum of x and y is: " + str(x + y))
#     print("The difference of x and y is: " + str(sub))  # Using sub variable
#     print("The quotient of x and y is: " + str(divide))  # Using divide variable
#     print("The product of x and y is: " + str(multiply))  # Using multiply variable
#     print("-" * 30)  # Separator for readability

# # Call the function
# add(10, 20)
# add(30, 40)
# add(50, 60)
# add(70, 80)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# create functions add, subtract, divide, multiply *THIS IS THE CORRECT WAY.*
# def add(x, y):
#     print (x + y)
# def subtract(x, y):
#     print (x - y)
# def divide(x, y):
#     print (x / y)
# def multiply(x, y):
#     print (x * y)

# add(10, 20)
# subtract(30, 40)
# divide(50, 60)
# multiply(70, 80)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Function with a return value *GREETINGS*
# def greet(name):
#     print("Hello, " + name + ". Good morning!")
# greet("John")   # Output: Hello, John. Good morning!
# greet("Jane")   # Output: Hello, Jane. Good morning!
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def greet(name, age):
#     print(f"Wassup, {name}, mananap!")
#     print(f"You are {age} years old.")

# greet("John", 36)
# greet("Jane", 21)
#~~~~~~~~~~~~~~~~###EXCERCISE###
# def greet(name, age, height, course):
#     print(f"Wassup, {name}, mananap!")
#     print(f"You are {age} years old.")
#     print(f"You are {height} centemeters tall.")
#     print(f"You are taking {course} course.")

# greet("John", 36, 170, "BSIT")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#First SAmple of a function with a return value
#1
# def add(x, y):
#     return x + y

# total = add(10, 20)

# print(total)
#2
# def calculate(x, y, operator):
#     if operator == "+":
#         return x + y
#     elif operator == "-":
#         return x - y
#     elif operator == "/":
#         return x / y
#     elif operator == "*":
#         return x * y
#     elif operator == "%":
#         return x % y
#     else:
#         return "Invalid operator"
    
# total = calculate(10, 20, "+")
# difference = calculate(10, 20, "-")
# qoutient = calculate(10, 20, "/")
# product = calculate(10, 20, "*")
# modulo = calculate(10, 20, "%")

# print (total)
# print (difference)
# print (qoutient)
# print (product)
# print (modulo)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def subtract(x, y):
#     return x - y
# def divide(x, y):
#     return x / y
# def multiply(x, y):
#     return x * y

# def add(x, y):
#     sub = x - y
#     divide = x / y
#     multiply = x * y
#     return x + y
# print("The value of x is: " + str(x))
# print("The value of y is: " + str(y))
# print("The sum of x and y is: " + str(x + y))

# add(10, 20)
# add(30, 40)
# add(50, 60)
# add(70, 80)


