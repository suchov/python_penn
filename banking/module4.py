# Implement all that stuff that is in module at the same time
# It'll be easy by coppy and paste and I can play with it a bit here
# don't forget about the main function...
def import_and_create_dictionary(filename):
    '''
    This function is used to create a bank dictionary.  The given argument is the filename to load.
    Every line in the file will look like
    key: value
    Key is a user's name and value is an amount to update the user's bank account with.  The value should be a
    number, however, it is possible that there is no value or that the value is an invalid number.

    What you will do:
    - Try to make a dictionary from the contents of the file.
    - If the key doesn't exist, create a new key:value pair.
    - If the key does exist, increment its value with the amount.
    - You should also handle cases when the value is invalid.  If so, ignore that line and don't update the dictionary.
    - Finally, return the dictionary.

    Note: All of the users in the bank file are in the user account file.
    '''

    d = {}

    # your code here
    f = open(filename, 'r')
    lines = f.readlines()

    for line in lines:
        # strip witespaces from the  begining and the end of line
        # split into a list based on coma separator
        lst = line.strip().split(',')

        # if the lenth of the list is less then one - skip this line
        if len(lst) <= 1:
            continue
        # get key (name) and value (expece ammount) from list 
        key = lst[0].strip()
        value = lst[1].strip()

        try:
            # cast value to float
            value = float(value)

            # look up for the key, if it exist add the value if not - set it to 0
            d[key] = d.get(key, 0) + value
        except:
            # oterwise go to the top of the for loop/to the next line
            continue


    f.close()
    
    return d


def import_and_create_accounts(filename):
    '''
    This function is used to create an user accounts dictionary and another login dictionary.  The given argument is the filename to load.
    Every line in the file will look like
      username - password

    If the username and password fulfills the requirement, add the username and password into the user accounts dictionary.
    To make sure that the password fulfills these requirements, be sure to use the signup function that you wrote above.
    
    For the login dictionary, the key is the username, and its value indicates whether the user is logged in, or not.
    Initially, all users are not logged in.

    Finally, return the dictionaries.

    Note: All of the users in the bank file are in the user account file.
    '''

    user_accounts = {}
    log_in = {}

    # your code here
    

    return user_accounts,log_in

def main():
    '''
    The main function is a skeleton for you to test if your overall programming is working.
    Note we will not test your main function. It is only for you to run and interact with your program.
    '''

    bank = import_and_create_dictionary("bank.txt")
    user_accounts, log_in = import_and_create_accounts("user.txt")

if __name__ == '__main__':
    main()