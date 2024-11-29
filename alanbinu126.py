def recursive_addition(num1,num2):
    if num2==0:
        return num1
    else:
        return recursive_addition(num1+1,num2-1)
num1=int(input('enter the number 1 '))
num2=int(input('enter the number 2'))
print(f"sum={recursive_addition(num1,num2)}")