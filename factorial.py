#program to display the factorial of a number
def factorial (x): #definiendo función
    if x < 0:
        return 0 #si el número es menor que cero, se devuelve 0
    elif x == 0 or x == 1:
        return 1 #si el número es igual a 0 o 1, se devuelve 1
    else:
        fact = 1
        while (x > 1): #mientras el número sea mayor a 1, el número se multiplica
            fact *= x
            x -= 1
        return fact #se devuelve el resultado

num = float(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
print("Thanks for using this program :)")
