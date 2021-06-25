# Python program to modify the
# content of binary file
 
 
# Function to update the
# content of binary file
def update_binary(word, neww)
    # string variable to store
    # each word after reading
    # from the file
    string = b""
 
    # Flag variable to check
    # if the record is found or
    # not
    Flag = 0
 
    # Open the file in r + b mode which means
    # opening a binary file for reding and
    # writing
    with open('file.txt', 'r + b') as file:
 
        pos = 0
 
        # Reading the content of the
        # file character by character
        data = string = file.read(1)
 
        # Looping till the end of
        # file is reached
        while data:
            data = file.read(1)
 
            # Checking if the space is reached
            if data == b" ":
 
                # checking the word read with
                # the word entered by user
                if string == word:
 
                    # Mpving the file pointer
                    # at the end of the previously
                    # read record
                    file.seek(pos)
 
                    # Updating the content of the file
                    file.write(new)
                    Flag = 1
                    break
                else:
                    # storing the position of
                    # current file pointer i.e. at
                    # the end of previously read record
                    pos = file.tell()
                    data = string = file.read(1)
            else:
 
                # Storing the data of the file
                # in the string variable
                string += data
                continue
 
 
    if Flag:
        print("Record successfully updated")
    else:
        print("Record not found")
         
         
# Driver code
# Input the word to be found
# and the new word
word = input("Enter the word to be replaced: ").encode()
neww = input("\nEnter the new word: ").encode()
 
update_binary(word, neww)