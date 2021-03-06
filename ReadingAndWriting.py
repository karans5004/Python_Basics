""" File Access Modes

Access modes govern the type of operations possible in the opened file. It refers to how the file will be used once its opened. These modes also define the location of the File Handle in the file. File handle is like a cursor, which defines from where the data has to be read or written in the file. There are 6 access modes in python.

    Read Only (‘r’) : Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exists, raises I/O error. This is also the default mode in which file is opened.
    Read and Write (‘r+’) : Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exists.
    Write Only (‘w’) : Open the file for writing. For existing file, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exists.
    Write and Read (‘w+’) : Open the file for reading and writing. For existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.
    Append Only (‘a’) : Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
    Append and Read (‘a+’) : Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

 """

""" # Program to show various ways to read and
# write data in a file.
file1 = open("MyFile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
  
# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes
  
file1 = open("MyFile.txt","r+") 
  
print ("Output of Read function is ")
print (file1.read())
print
  
# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0) 
  
print ("Output of Readline function is ")
print (file1.readline())
print
  
file1.seek(0)
  
# To show difference between read and readline
print ("Output of Read(9) function is ")
print (file1.read(9))
print
  
file1.seek(0)
  
print ("Output of Readline(9) function is ")
print (file1.readline(9))
  
file1.seek(0)
# readlines function
print ("Output of Readlines function is ")
print (file1.readlines())
print
file1.close() """

#Appeding to a File

""" # Python program to illustrate
# Append vs write mode
file1 = open("MyFile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
file1.close()
  
# Append-adds at last
file1 = open("MyFile.txt","a")#append mode
file1.write("Today \n")
file1.close()
  
file1 = open("MyFile.txt","r")
print "Output of Readlines after appending"
print file1.readlines()
print
file1.close()
  
# Write-Overwrites
file1 = open("MyFile.txt","w")#write mode
file1.write("Tomorrow \n")
file1.close()
  
file1 = open("MyFile.txt","r")
print "Output of Readlines after writing"
print file1.readlines()
print
file1.close() """