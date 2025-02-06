# While loop

# num = 3

# while num > 0:
#     print(f"{num} is greater than ZERO.")
#     num -= 1

#     #=================================================================

# num = int(input("Enter a number: "))

# while num * 3 < 10:
#     print(f"{num} * 10 = {num * 10}")
#     num -= 1
    #=================================================================
#BASIC ROOT
# num = 1

# while num <= 10:
#     print(num)
#     num += 1
    #=================================================================
#---------------------CGPT
# Ask the user for a number
# number = int(input("Enter a number: "))

# # Initialize the loop counter
# i = 1

# # Generate and display the multiplication table from 1 to 10 using a while loop
# print(f"Multiplication table for {number}:")
# while i <= 10:
#     print(f"{number} x {i} = {number * i}")
#     i += 1  # Increment the loop counter
    #=================================================================
#---------------------GRN
# userinput = int(input("Enter a number: "))

# iterator = 1

# while iterator <= 10:
#     product = userinput * iterator
#     print(f"{userinput} x {iterator} = {product}")
#     iterator = iterator + 1
    #=================================================================
#EXCERCISES
#MY X FORMULA!
# userinput = int(input("Enter a number: "))

# iterator = 1

# while iterator <= userinput:
#     print(userinput)
#     userinput += 1

#RIGHT FORMULA!
# userinput = int(input("Enter a number: "))  
# iterator = 1    
# while iterator <= userinput:
#     print(iterator)
#     iterator += 1
    #=================================================================
# Exercise 1
# # Ask the user for a number
# number = int(input("Enter a number: "))

# # Initialize the counter
# i = 1

# # Generate and display the multiplication table from 1 to 10
# print(f"Multiplication table for {number}:")
# while i <= 10:
#     print(f"{number} x {i} = {number * i}")
#     i += 1  # Increment the counter
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercise 2
# # Initialize a counter
# count = 0

# # Use a while loop to print "Hello, World!" 5 times
# while count < 5:
#     print("Hello, World!")
#     count += 1  # Increment the counter
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercise 3
# # Initialize the total sum
# total_sum = 0

# # Loop to keep asking for numbers until the user enters 0
# while True:
#     number = int(input("Enter a number (0 to quit): "))
#     if number == 0:
#         break  # Exit the loop if the user enters 0
#     total_sum += number  # Add the number to the total sum

# # Display the total sum
# print(f"Total sum: {total_sum}")
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercise 4
# # Ask the user for a positive integer
# number = int(input("Enter a positive integer: "))

# # Ensure the number is positive
# if number < 0:
#     print("Please enter a positive integer.")
# else:
#     # Use a while loop to count down to zero
#     while number >= 0:
#         print(number)
#         number -= 1  # Decrease the number by 1 in each iteration
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
