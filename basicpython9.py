'''
Name:Alan Binu
Date:25-10-2024
Description:a Python program to convert temperature values back and forth between Celsius and Fahrenheit.
The user should be able to input a temperature in Celsius or Fahrenheit,
and the program should convert it to the other unit using the formula:
'''
temp=int(input('enter the temperature'))
scale=input(' is this in (C)elsius or (F)ahrenheit?')
if scale=="C":
    result_C=(9/5*temp)+32
    print(temp,'Celsius is',result_C,'Fahrenheit')
else:
    result_F=5/9*(temp+32)
    print(temp,'Fahrenheit is',result_F,'Celsius')
