# # def square function
# # takes on number as a paramether
# # returns the result of squaring that number

# def square(x):
#     y = x * x
#     return y

# print(square(10))

# def grater_than(x, y):

#     if x > y:
#         return True
#     else:
#         return False

# print(grater_than(1, 10))

# def greater_than(x, y):
#     """Returns True if x is greater than y, otherwise False."""
    
#     if x > y:
#         return True
#     else:
#         return False

# #prints general help on the function, including the docstring    
# help(greater_than)

# def get_factors(x):
#     """Returns a list of factors of given number x"""
#     factors = []
#     # iterate over range from 1 to number x 
#     for i in range(1, x + 1):
#         # check if i divide number x evenly
#         if (x % i == 0):
#             factors.append(i)
#     return factors

# print(get_factors(21))

def unique_list(array):
    """Returns a unique list from a list given as a param"""
    unique_array = []
    for x in array:
        if x not in unique_array:
            unique_array.append(x)
    return unique_array

print(unique_list([1, 11, 12, 1, 12, 4]))