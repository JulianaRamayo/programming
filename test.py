import random

def guess(intento = 1):
    randomNumber = random.randint(1, 10)
    correct = False
    if intento <= 4:
        while not correct:
            user_guess = int(input("Guess a number between between 1 and 10 \^o^/: "))
            if user_guess < randomNumber: #if the user inputs a number that is low compared to the random number, it prints the message
                print("Looks like this number is too low. Try again :(")
            elif user_guess > randomNumber: ##if the user inputs a number that is high compared to the random number, it prints the message
                print("Looks like this number is too high. Try again :(")
            elif user_guess == randomNumber:
                print("This is the right number! Well done <3")
                correct = True
                return None
            intento += 1
            print(intento)
            guess(intento)
    if intento > 4:
        print("Looks like you haven't guess the number. Sorry. You lost")
        return None

guess(intento = 5)
guess()
