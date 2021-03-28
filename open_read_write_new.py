# create an open_read_write_new_file(file1, file2) - copy the text from one file to another file

def open_read_write_new_file(file1, file2):
    """Open the first file, and read all all the text as a string
    Copies or writes all the text to the second file."""

    # open the file for the reading
    with open(file1) as fin:
        #read all lines as a single string
        text = fin.read()
    
        # open second file in a write mode
        fout = open(file2, 'w')

        # write single string to second file
        fout.write(text)

        # clouse second file
        fout.close()

    
def main():

    open_read_write_new_file('news.txt', 'news_copy.txt')

if __name__ == '__main__':
    main()
