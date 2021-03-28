# create an open_read_append_same_file() 

def open_read_append_same_file(file):
    """Open the first file, and read all lines into a list,
    Reverses the lines, and appends then to the second file."""

    # open the file for the reading and writing
    f = open(file, "r+")

    # read all lines into a list
    lst = f.readlines()

    # updating list before appending back to the same file
    lst.insert(0, '\n')
    lst.insert(0, 'here is some new text')
    lst.insert(0, '\n')

    # append the lines back to the same file
    f.writelines(lst)

    f.close()


    
def main():

    open_read_append_same_file("news.txt")

if __name__ == '__main__':
    main()
