# This program checks whether a triangle is equilateral, isosceles or scalene.
otherOperation = "Y"
while otherOperation == "Y":
    A = float(input("Enter one side: "))
    B = float(input("Enter the second side: "))
    C = float(input("Enter the last side: "))
    # First, ask for the triangle's sides.
    if A == B and B == C and A == C:
        print("This triangle is equilateral")
        otherOperation = input("Do yo want to try again? (Y/N): ").upper()
    elif A == B or A == C or B == C:
        print("This triangle is isosceles")
        otherOperation = input("Do yo want to try again? (Y/N): ").upper()
    elif A != B and B != C and A != C:
        print("This triangle is scalene")
        otherOperation = input("Do yo want to try again? (Y/N): ").upper()
    else:
        print("Invalid operation")
print("Thank you for using this program. Bye! <3 uwu")
#Check conditions.