# This program finds the maximum between two numbers.
otherOperation = "Y"
while otherOperation == "Y":
    A = float(input("Enter a number: "))
    B = float(input("Enter another number: "))
    # First, ask for the two numbers.
    if A < B:
        print("The maximum number is", B)
        otherOperation = input("Do yo want to try again? (Y/N): ").upper()
    elif A > B:
        print("The maximum number is", A)
        otherOperation = input("Do yo want to try again? (Y/N): ").upper()
    elif A == B:
        print("The numbers are equal")
        otherOperation = input("Do yo want to try again? (Y/N): ").upper()
    else:
        print("Invalid operation")
print("Thank you for using this program. Bye! <3")
#Check both numbers.