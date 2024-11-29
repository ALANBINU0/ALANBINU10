def re_factorial(n):
    if n==1:
        return 1
    else:
        return n*re_factorial(n-1)
n=int(input('enter your number'))
print(re_factorial(n))
