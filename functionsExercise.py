print("Exercise 1: Create a function in Python")
print("Instruction: Write a program to create a function that takes two arguments, name and age, and print their value.")
def name_and_age(name, age):
    #print the values.
    print("Name:", name, " Age:", age)
#call the function
name_and_age("Ben", 25)

print("Exercise 2: Create a function with variable length of arguments")
print("Instruction: Write a program to create function func1() to accept a variable length of arguments and print their value.")
#define function.
def func1(*args):
    for numbers in args:
        print(numbers)
#call the function
print("First Time")
func1(20, 40, 60)
print("Second Time")
func1(80, 100)

print("Exercise 3: Return multiple values from a function")
print("Instruction: Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.")
#declare function.
def calculation (a, b):
    addition = a + b
    substraction = a - b
    print ("The result of the addition is ", addition, "and the result of the substraction is ", substraction)

#call function
calculation(40, 10)

print("Exercise 4: Create a function with default argument")
print('''Instruction: Write a program to create a function show_employee() using the following conditions.
*It should accept the employee’s name and salary and display both.
*If the salary is missing in the function call then assign default value 9000 to salary''')
def show_employee(name, salary = 9000):
    print("Name:", name, "  salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")

print("Exercise 5: Create an inner function to calculate the addition in the following way")
print('''*Create an outer function that will accept two parameters, a and b
*Create an inner function inside an outer function that will calculate the addition of a and b
*At last, an outer function will add 5 into addition and return it''')
#declare outer function
def outer_fun(a, b):
    square = a ** 2

    #declare inner function
    def addition(a, b):
        return a + b

    #call inner function from outer function
    add = addition(a, b)
    #add 5 to the result
    return add + 5

result = outer_fun(5, 10)
print("The result is: ", result)

print("Exercise 6: Create a recursive function")
print("Instruction: Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.")
def recursive(num):
    if num:
        return num + recursive(num - 1)
    else:
        return 0

res = recursive(10)
print(res)

print("Exercise 7: Assign a different name to function and call it through the new name")
print("Instruction: Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.")
#declare function
def display_student(name, age):
    print(name, age)

display_student("Emma", 26)
#assign a new name
show_student = display_student
#call with new name
show_student("Emma", 26)

print("Exercise 8: Generate a Python list of all the even numbers between 4 to 30")
print(list(range(4, 30, 2)))

print("Exercise 9: Find the largest item from a given list")
x =  [4, 6, 8, 24, 12, 2]
print(x)
print(max(x))

print("End :)")