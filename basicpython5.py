'''
Author:Alan Binu
Date:19-10-2024
Description:a Python program that performs the following tasks:
    User Input:
        Ask the user to enter two numbers, num1 and num2.
        Ask the user to enter a third number, num3.

    Addition:
        Add the first two numbers (num1 and num2).
        Print the sum in the format: "The sum of num1 and num2 is: result"

    Subtraction:
        Subtract num2 from num1.
        Print the difference in the format: "The difference when num2 is subtracted from num1 is: result"

    Multiplication:
        Multiply num1 by num2.
        Print the product in the format: "The product of num1 and num2 is: result"

    Division:
        Divide num1 by num2.
        Print the quotient in the format: "The quotient when num1 is divided by num2 is: result"

    Modulus:
        Find the remainder when num1 is divided by num2.
        Print the remainder in the format: "The remainder when num1 is divided by num2 is: result"

    Combined Arithmetic Operation:
        Perform the following combined operation:
        result = (num1 + num2) * num3 / 2
        Print the result in the format: "The result of (num1 + num2) * num3 / 2 is: result" result"



'''
num1=int(input("enter the first no"))
num2=int(input("enter the second no"))
num3=int(input("enter the third no"))
add=num1+num2
print('The sum of num1 and num2:',add)
subt=num1-num2
print('The difference when num2 is subtracted from num1 is:',subt)
mult=num1*num2
print("The product of num1 and num2 is: mult")
div=num1/num2
print("The quotient when num1 is divided by num2 is: div")
mod=num1%num2
print( "The remainder when num1 is divided by num2 is: mod")
ari=(num1+num2)*num3/2
print("The result of (num1 + num2) * num3 / 2 is: ari")
