# create an import_and_create_dictionary(filename): 

def import_and_create_dictionary(filename):
    """This function is create an expense dictionary from a file.
    Every line in the file should be in the format:
        key, value
    The key is a user's name and the value is an expense to update the users
    total expense with.
    The value should be a number, hovever it is possible that there is no value,
    that the value is invalid number, or that the entire line is blank."""

    expenses = {}

    # open file in read mode and read all the lines into a list
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
            expenses[key] = expenses.get(key, 0) + value
        except:
            # oterwise go to the top of the for loop/to the next line
            continue


    f.close()

    return expenses

    
def main():

    expenses = import_and_create_dictionary("expenses.txt")
    print("expenses:", expenses)

if __name__ == '__main__':
    main()
