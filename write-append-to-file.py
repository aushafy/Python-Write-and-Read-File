"""
another write program function to add some text in the file which has the content before.
"""
filename = "listofname.txt" # type file name which you want to add some text inside that
with open(filename, "a") as file_obj: # open() function with 'a' argument to appending text in file which has content
    file_obj.write("\n9. Yunus") # sample instance