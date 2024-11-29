def phone():
    n=input('enter the phone no:')
    if len(n)==10 and n[0] in "7,8,9":
        print('it is a valid no')
    else:
        print('it is not a valid no')
phone()

