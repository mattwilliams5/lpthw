#!/usr/local/bin/python3

from sys import argv

# setting two parameters one for the file and another for our text file
script, filename = argv
# Opening our text file
txt = open(filename)

#displaying the file name
print(f"Here's your file {filename}:")

# Reading the file.
print(txt.read())
txt.close()
#displaying the file name again
print("Type the filename again:")

#Setting a prompt
file_again = input("> ")
# Opening the file
txt_again = open(file_again)

# Reading the file again
print(txt_again.read())
txt_again.close()
