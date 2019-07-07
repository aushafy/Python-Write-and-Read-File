"""
Simple program to write an instance to a file.

open() argument: 'w' to write in empty file, 'a' to appending to a file.
"""
filename = 'empty.txt' # select file that you want to add some text inside.
with open(filename, 'w') as file_obj: # open function with 'w' argument it is mean you will add some text in empty file
    file_obj.write("I love programming!\n") # write() function to writes some text inside files
    file_obj.write("I love Python!\n") # to write multiple lines with \n in the end of line