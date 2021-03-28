# create an open_read_append_new_file function that opens reads one file, reverse the text, then appends the reversed text to another file

def open_read_append_new_file(file1, file2):
    """Open the first file, and read all lines into a list,
    Reverses the lines, and appends then to the second file."""

    # open the first file in the read mode
    with open(file1) as fin:
        # read all lines into a list
        lst = fin.readlines()

        # reverse the list
        lst.reverse()

        # open second file for pending
        fout = open(file2, "a")

        # write reversed lines to a second file
        fout.writelines(lst)

        # close the second file
        fout.close()

    
def main():

    open_read_append_new_file("news.txt", "news_out.txt")

if __name__ == '__main__':
    main()
