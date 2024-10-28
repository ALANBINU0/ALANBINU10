'''
Name:Alan Binu
Date:28-10-2024
Description:a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit.
The program should repeatedly display a menu with three options:
'''
while True:
    print('1.\tConvert Celsius to Fahrenheit')
    print('2.\tConvert fahrenheit to celsius')
    print('3.\tExit the program')
    choice=int(input('enter the choice'))
    if choice==1:
        temp_celsius=int(input('enter the temperature in celsius'))
        temp_faren=(temp_celsius* 9/5) + 32
        print(temp_celsius,"celsius in fahrenheit is",temp_faren)
    elif choice==2:
        temp_faren=int(input('enter the temperature in fahrenheit'))
        temp_celsius=(temp_faren-32) * 5/9
        print(temp_faren,"fahrenheit in celsius is",temp_celsius)
    elif choice==3:
        break
    else:
        print('invalid entry')