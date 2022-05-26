# This program dheck whether a number is negative, positive or zero.
otherOperation = "Y"
while otherOperation == "Y":
    A = float(input("Enter a number: "))
    # First, ask for the number.
    if A < 0:
        print("This number is negative")
        otherOperation = input("Do yo want to try again? (Y/N): ").upper()
    elif A > 0:
        print("This number is positive")
        otherOperation = input("Do yo want to try again? (Y/N): ").upper()
    elif A == 0:
        print("This number is equal to zero")
        otherOperation = input("Do yo want to try again? (Y/N): ").upper()
    else:
        print("Invalid operation")
print("Thank you for using this program. Bye! <3 uwu")
#Check both numbers.