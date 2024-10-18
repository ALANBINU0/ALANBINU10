'''
Author:Alan Binu
Date:18-10-2024
Description= a Python program that uses functions from the math module to perform
the following operations on a number provided by the user:
enter a number9
square root of 9 : 3.0
factorial of  9 : 362880
9 to the power of 2 : 81.0

'''



import math
number=int(input('enter a number'))
square_root=math.sqrt(number)
print('square root of',number,':',square_root)
factorial=math.factorial(number)
print('factorial of ',number,':',factorial)
power=(math.pow(number,2))
print(number,'to the power of 2 :',power)
