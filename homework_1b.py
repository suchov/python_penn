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

dog_age = input("How old is you dog? ")

human_age = int(dog_age) * 2

print(f"The given dog age {dog_age} is {human_age} in human years.")