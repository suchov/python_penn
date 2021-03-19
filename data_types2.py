# name = "Artem Sychov"

# print(name[:name.index(' ')])

# colors = 'blue,red,green'
# colors_list = colors.split(',')

# print(colors_list)
# print(colors_list[2])

# # Tuples are imutable

# direction = ('north', 'south', 'east', 'west')
# print(direction)

def max_and_min(list):
    """Returns max and min of given list."""

    # return tuple containig max and min of list
    return (max(list), min(list))

def main():
    list1 = [10, -1, 34, 56]   
    maxandmin = max_and_min(list1)

    # first, take a look at the type
    print(type(maxandmin))
    print(maxandmin)

if __name__ == '__main__':
    main()