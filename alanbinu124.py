def right_triangle():
    a1=[]
    s1=int(input('enter the first side'))
    a1.append(s1)
    s2=int(input('enter the second side'))
    a1.append(s2)
    s3=int(input('enter the third side'))
    a1.append(s3)
    a1.sort()
    if a1[2]**2==a1[0]**2+a1[1]**2:
        print('it is a right triangle')
    else:
        print('it is not a right triangle')
right_triangle()