"""
Read from a file (Cont.) is a method to storing the lines in a list.
"""
filename = 'listofname.txt' # select file by type file name
with open(filename) as file_obj:
    lines = file_obj.readlines()

for line in lines:
    print(line.rstrip())