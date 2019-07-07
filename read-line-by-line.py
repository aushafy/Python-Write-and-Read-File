"""
Previously, we have been make program that can be open and read entire of file.
in this capter, we will make another program that can be read file's content line-by-line.
"""
filename = 'listofname.txt' # select file by type file name
with open(filename) as file_obj: # open file with open() function and make alias name from filename (file_obj)
    for line in file_obj: # using for looping to read entire content line-by-line
        print(line.rstrip()) # we used rstrip() funtion to remove trailing spaces. it makes contents readable