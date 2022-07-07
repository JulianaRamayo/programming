#Python program that accepts a filename from the user and print the extension of that.
filename = input("Please write the filename: ")
f_extension = filename.split(".")
print("The extension of the file is: " + repr(f_extension[-1]))