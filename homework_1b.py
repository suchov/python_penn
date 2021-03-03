# Getting user input
# Error checking
# Variables & data types
# Conditionals 

# Write the program that calculates a dog's age in human years

# Prompt the users for an age in dog years
# Calc that age in human years
# Allow ints or floats
# Check if the input is valid(numeric and positive)
# prompt the error if not valid

# rules to approximately convert:

# For the first year, one dog year is equal to 15 human years
# For the first 2 years, each dog year is equal to 12 human years
# For the first 3 years, each dog year is equal to 9.3 human years
# For the first 4 years, each dog year is equal to 8 human years
# For the first 5 years, each dog year is equal to 7.2 human years
# After that, each dog year is equal to 7 human years.  
# (Note: This means the first 5 dog years are equal to 36 human years (5 * 7.2) 
# and the remaining dog years are equal to 7 human years each.)

# Results example "The given dog age <dog_age> is <human_age> in human years." 
# Round the result to 2 decimal places.
# Note: If there is a 0 in the hundredths place, you can drop it, e.g. 24.00 can be displayed as 24.0.
# make sure that your code can handle negative value inputs and non-numerical inputs!

# If a text-based input is provided, make sure your response contains the word 'invalid'.  
# For example, if the user doesn’tinput a number, print “<age> is invalid.”, substituting for <age>.

# If a negative input is provided, make sure your response contains the word 'negative'.  
# For example, if the user inputs a negative number, print “Age cannot be a negative number.”
import re

age = input("How old is you dog? ")

dog_age = float(age)

if dog_age < 0:
    print("The number can't be negative")

human_age = dog_age * 2.0
hhuman_age = "The given dog age {} is {} in human years.".format(age, human_age)

print(f"The given dog age {age} is {human_age} in human years.")
print(hhuman_age)

hhhhuman_age = re.findall("\d+\.\d+ in human", hhuman_age)
print("fff {}".format(hhhhuman_age))


# DOG AGE TO HUMAN AGE calculator

# import traceback

# def calculator():
    
#     # Get dog age
#     age = input("Input dog years: ")

#     try:
#         # Cast to float
#         d_age = float(age)

#         # If user enters negative number, print message
#         # Otherwise, calculate dog's age in human years
        
#         # your code here
        
#         if d_age < 0:
#             print("The number can't be negative")
#         elif d_age == 1:
#             human_age = 15.0
#         elif d_age == 2:
#             human_age = 24.0
#         elif d_age == 3:
#             human_age = 27.9
#         elif d_age == 4:
#             human_age = 32.0
#         elif d_age == 5:
#             human_age = d_age * 7.2
#         else:
#             human_age = (5 * 7.2) + (d_age - 5) * 7
            
#         print("The given dog age {} is {} in human years.".format(age, human_age))

#     except:
#         print(age, "is an invalid age.")
#         print(traceback.format_exc())
    
# calculator()