"""
Reading an entire file at once.

Algorithm: Open file with open() function and then read content of the file with read() function
"""

filename = 'listofname.txt' # select file

with open(filename) as file_obj: # open file with open() function
    content = file_obj.read() # read entire content of file with read() function

print(content)