#This program is a game where you can play to guess the number with the computer.
import random

def userGuess(x): #this function is used to guess a random number from the computer
    randomNumber = random.randint(1, x)
    guess = 0
    while guess != randomNumber: #if the user hasn't guess the number, it enters a while loop
        guess = int(input(f"Guess a number between between 1 and {x} \^o^/: \n"))
        if guess < randomNumber: #if the user inputs a number that is low compared to the random number, it prints the message
            print("Looks like this number is too low. Try again :(")
        elif guess > randomNumber: ##if the user inputs a number that is high compared to the random number, it prints the message
            print("Looks like this number is too high. Try again :(")
    print("This is the right number! Well done <3") #if the user guesses the number correctly, then the round ends.

def computerGuess(x): #this function is used to guess a random number from the user
    print('''Please, think about a number...
And do not change it while playing this round T-T''')
    low = 1
    high = x
    feedback = ""
    while feedback != "c": #if the feedback is not equal to c (correct), then the program keeps running
        if low != high:
            guess = random.randint (low, high)
        else:
            guess = high
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)? \^o^/\n").lower()
        if feedback == "h":
            high == guess - 1
        elif feedback == "l":
            low == guess + 1
    print(f'''Your number is {guess}, right?
Looks like I have guessed the number ~^o^~''')


otherRound = "Y"
print("Hello! Welcome to 'Guess the number' \^o^/")
userName = str(input("Please write your name ~^o^~: "))
while otherRound == "Y": #a loop to keep playing the game for a undeterminated number of rounds.
    guesser = int(input(f'''Nice to meet you, {userName} \^o^/
Who guesses in this round?
1. You guess the number.
2. I guess the number \n'''))
    if guesser == 1:
        userGuess(30)
        otherRound = input("Do you want to play again? (Y/N): ").upper()
    elif guesser == 2:
        computerGuess(30)
        otherRound = input("Do you want to play again? (Y/N): ").upper()
    else:
        print("Looks like you have chosen an invalid option T-T")
        otherRound = input("Do you want to try again? (Y/N): ").upper()
print('''Thank you for playing this game \^o^/
I had a lot of fun while playing with you!
Hope to see you soon T-T
Bye, bye!! <3''')