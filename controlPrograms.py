#this program works with .txt files.

#function to read the poem.txt file
def read (): 
    file = open("poem.txt", mode="r") #file is declared by opening the .txt file and mode r because is for reading
    for line in file: #for loop to print all the lines of the poem
        print(line)  #print function
    file.close() #the file is closed with the close function

#function to count the lines that do not start with T
def countLines(): 
    file = open("story.txt", mode="r") #to open the file and to assign the file a name
    count = 0 #variable to count the lines

    print("\nIn this story the following lines do not start with T: ")
    for line in file: #for loop to check each line
        if line[0] not in "T": #if the line does not start with T then it prints that line and keeps counting
            print(line)
            count = count + 1
    file.close() #the file is closed
    print(count, "lines do not start with T") #to print the quantity of lines do not start with T

#function to count the words in the file
def numberOfWords():
    file = open("poem.txt", mode="r") #to open the file and to assign the file a name
    count = 0 #variable to count the words
    text = file.read() #read function to read the content of the file
    words = text.split() #split function to make the string a list
    for word in words: #loop to count the number of words
        count = count + 1
    print("\nThere are", count, "words in the file")
    file.close() #to close the file

#function to count how many times "the" is repeated
def theCount():
    file = open("note.txt", mode="r") #to open the file and to assign the file a name
    count = 0 #variable to count the times "the" is repited
    text = file.read() #function to read the content of the file
    words = text.split() #function to make the string a list
    for word in words: #for loops to test each word
        if word == "The" or word == "the": #if the condition is applied then the variable increases
            count = count + 1
    print("\n'The' is printed", count, "times")
    file.close()


otherFunction = "Y" #variable to keep running the program
while otherFunction == "Y": #while loop to keep running the program
    function = int(input('''Select function:
    1. Read poem.txt
    2. Count the lines from story.txt that do not start with T
    3. Count the total number of words in a poem.txt
    4. Count the number of times 'the' is repited in note.txt\n''')) #options are displayed and input from the user is taken

    if function == 1: #if user chooses first option
        print("Poem: ")
        read() #the function is executed
        otherFunction = input("Do yo want to do try another function? (Y/N): ").upper() #option to keep running the program
    elif function == 2: #if user chooses second option
        print("The text that will be checked is: ")
        with open("story.txt") as file: #to assign the file a variable
            print(file.read()) #to print the text inside the file
        file.close() #to close the file
        countLines() #the function is executed
        otherFunction = input("Do yo want to do try another function? (Y/N): ").upper() #option to keep running the program
    elif function == 3: #if user chooses third option
        print("The text that will be checked is: ")
        read() #to print the text
        numberOfWords() #function is executed
        otherFunction = input("Do yo want to do try another function? (Y/N): ").upper() #option to keep running the program
    elif function == 4: #if user chooses fourth option
        print("The text that will be checked is: ")
        with open("note.txt") as file2: #to assign note a variable
            print(file2.read()) #to print the text inside the file
        file2.close() #to close the file
        theCount() #function is executed
        otherFunction = input("Do yo want to do try another function? (Y/N): ").upper() #option to keep running the program
    else: #if user tries to choose another option
        print("You choosed an invalid operation")
        otherOperation = "Y"
print("Thank you for using this program. Bye.")