#this function calculates different aritmetic operations.
def add (A, B):
    add = A + B
    print(add)
    #this function adds two numbers
    
def sub (A, B):
    sub = A - B
    print(sub)
    #this function substracts two numbers
    
def mul (A, B):
    mul = A * B
    print(mul)
    #this function multiplies two numbers

def div (A, B):
    div = A / B
    print(div)
    #this function divides two numbers

otherOperation = "Y"
while otherOperation == "Y":
    operation = int(input('''Select operation:
    1. Add
    2. Substract
    3. Multiply
    4. Division\n'''))
    A = float(input("Enter a number:"))
    B = float(input("Enter another number:"))
    
    
    if operation == 1:
        add(A, B)
        otherOperation = input("Do yo want to do another operation? (Y/N): ").upper()
    elif operation == 2:
        sub(A, B)
        otherOperation = input("Do yo want to do another operation? (Y/N): ").upper()
    elif operation == 3:
        mul(A, B)
        otherOperation = input("Do yo want to do another operation? (Y/N): ").upper()
    elif operation == 4:
        div(A, B)
        otherOperation = input("Do yo want to do another operation? (Y/N): ").upper()
    else:
        print("You choosed an invalid operation")
        otherOperation = "Y"
print("Thank you for using this program. Bye.")