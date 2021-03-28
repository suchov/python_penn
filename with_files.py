# work with files - open, work, close
# open(path_to_file, mode) 'r' - read, 'w' - write, 'a' - append mode, 'r+' - read and write / r is default
# stream.read() - reads all text in the file
# stream.readline() - reads one line in the file
# stream.readlines() - reads all lines in the file as a list
# stream.close() - don't forget to close the stream at the end
# \n - the new line rstrip() - method that removes this char example:

# line = stream.readline()
# line.rstrip()

# or if iterating over a stream directly:

# for line in open(file, "r"):
#     line.rsplit() # removes whitespace, including \n char, at the end

# stream to write a string to a file

# stream.write(string)

# stream.writelines(list_of_strigs)

# stream.close() # - when done cause you can't open it again until it closed ...

# will automatically close the file for you after the statements have been executed
# with open(my_file, 'w') as stream:
#     # statements using the file object

# create an open_read_file function that opens a file, reads each line and prints it to the console

def open_read_file(file):
    """Opens the given file, reads each line and prints to the console.
    Closes the given file."""
    
    # open the given file in a read mode
    f = open(file, "r")
    print(type(f)) # print the type of the stream f

    cnt = 0 # counter for the lines in the file

    # reads and prints each line in f, while there is a line to read
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()

        cnt += 1

    print('')
    print('there are', cnt, 'lines in the file')

    f.close() # don't forget to close the file

def main():

    open_read_file('news.txt')

if __name__ == '__main__':
    main()