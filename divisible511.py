# This program dhecks whether a number is divisible by 5 and 11 or not.
otherOperation = "Y"
while otherOperation == "Y":
    A = float(input("Enter a number: "))
    # First, ask for the number.
    if A % 5 == 0 and A % 11 == 0:
        print("This number is divisible by both 5 and 11")
        otherOperation = input("Do yo want to try again? (Y/N): ").upper()
    elif A % 5 == 0:
        print("This number is only divisible by 5")
        otherOperation = input("Do yo want to try again? (Y/N): ").upper()
    elif A % 11 == 0:
        print("This number is only divisible by 11")
        otherOperation = input("Do yo want to try again? (Y/N): ").upper()
    elif A % 5 != 0 and A % 11 != 0:
        print("This number is neither divisible by 5 nor 11")
        otherOperation = input("Do you want to try again? (Y/N): ").upper()
    else:
        print("Invalid operation")
print("Thank you for using this program. Bye! <3 uwu")
#Checar si los número cumplen  la candición.