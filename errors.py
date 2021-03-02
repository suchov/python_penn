number = input('Please input an integer.')
#Try to cast the input
try:
    number = int(number)
#Catch the raised exeption if there is an error
except ValueError as e:
    print("Your input is not an ingeter.")
    print(e)
#Otherwise, there is no error
else: 
    print(str(number) + " is indeed an integer!")
