# while loop to test a user input of a secret password

# - if the user input "secret", print "Welcome" and exit the program
# - otherwise, pring "Sorry, the password you enter is incorrect. Please try again." and prompt the user again

inp = input("Hi! Please enter the password. ")
print("")
while inp != 'secret':
    inp = input("Sorry, the password you enter is incorrect. Please try again. ")
    print("")

print('Welcome!')