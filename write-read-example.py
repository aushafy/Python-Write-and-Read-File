"""
This program was made to write-and-read data in some file.
User is allowed to input some text inside some file and check wheter the text already write successfully.

Algorithm:
1. User input file name that will be selected for the write-operation.
2. After that, we will make sure that file was successfully opened
3. If the file already successfully opened. next, user can input some text
4. If user input some text successfully, it will be automatically writes in file which selected before.
5. Last, checking wheter text is successfully write inside the text or nope.
"""

filename = input('Select file that you want to write-read: ') # user should select some file
with open(filename, 'w') as file_object: # open file function with 'w' argument to allows write some text
    print('File has been opened successfully!\n') # if file successfully opened, this program will be shown
    text = input('Text that you want to add: ') # if file has been successfully opened. 
    # it will be allowed user to input some text
    file_object.write(text) # write function to write text to file

# make sure that we have successfully add some text inside that file with read function
with open(filename) as read_object: # again, we open the file
    content = read_object.read() # read function to check wheter there is any text inside that file

if text in content: # check wheter text already added successfully.
    print('You have been successfully to add text to your file!') # if text successfully added. print text!
    print('Your text : ' + text)