'''
Author:Alan Binu
Date:18-10-2024
Description:a Python program that demonstrates the usage of arithmetic, comparison, and logical operators.
 Perform a few operations and print the results.
 enter the first number10
enter the second number5
sum= 15 ,division= 2.0
Is number1 greater than number2?: True
Are number1 and number2 equal?: False
Logical AND: True
Logical OR: False

Process finished with exit code 0


'''
number1=int(input('enter the first number'))
number2=int(input('enter the second number'))
print('sum=',number1+number2,",division=",number1/number2)
print('Is number1 greater than number2?:',number1>number2)
print('Are number1 and number2 equal?:',number1==number2)
print('Logical AND:',number1>0 and number2>0)
print('Logical OR:',number1<0 or number2<0)