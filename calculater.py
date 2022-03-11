
# CALCULATOR PROGRAM
# from numpy import matrix
from sys import exit
from math import factorial, pi, sqrt, sin, cos, tan, radians, log2, log10

# SIN,COS,TAN,COT,SEC,COSINE VALUES FOR INPUT D


def trig(d):
    if d == 1 or d == 6:
        e = input(' ENTER RADIANS : ')
        if e.isdigit():
            e = int(e)
            if d == 1:
                print((sin(radians(e))).__round__(2))
            else:
                try:
                    print((1//sin(radians(e))).__round__(2))
                except ZeroDivisionError:
                    print(' NOT DETERMINED(INFINITY) ')
        else:
            print(' INVALID ENTRY ')
    elif d == 2 or d == 5:
        e = input(' ENTER RADIANS : ')
        if e.isdigit():
            e = int(e)
            if d == 1:
                print(cos(radians(e)).__round__(2))
            else:
                try:
                    print((1 // cos(radians(e))).__round__(2))
                except ZeroDivisionError:
                    print(' NOT DETERMINED(INFINITY) ')
        else:
            print(' INVALID ENTRY ')
    elif d == 3 or d == 4:
        e = input(' ENTER RADIANS : ')
        if e.isdigit():
            e = int(e)
            if d == 1:
                print(tan(radians(e)).__round__(2))
            else:
                try:
                    print((1 // tan(radians(e))).__round__(2))
                except ZeroDivisionError:
                    print(' NOT DETERMINED(INFINITY) ')
        else:
            print(' INVALID ENTRY ')
    else:
        print(' INVALID CHOICE ')
        exit(0)

# LOG BASE 2 OF A AND LOG BASE 10 OF A



def logm(a):
    if a == 1:
        v = input(' ENTER A VALUE : ')
        v = checkisdigit(v)
        print(log2(v).__round__(2))

    else:
        v = input(' ENTER A VALUE : ')
        v = checkisdigit(v)
        print(log10(v).__round__(2))

# RETURNS INTEGER VALUE OF G IF G IS A DIGIT ELSE TERMINATES THE PROGRAM


def checkisdigit(l):
    try:
        return int(l)
    except ValueError:
        try:
            return float(l)
        except ValueError:
            print(' Invalid Entry ')
            exit()


print(' A SIMPLE CALCULATOR ')
print(' 1 : ARITHMETIC \n 2 : MATRIX \n 3 : TRIGONOMETRY \n 4 : FACTORIAL \n 5 : AREA \n 6 : PERIMETER \n 7 : LOGARITHMIC \n 8 : SQUARE ROOT \n 9 : CLOSE \n')
c = input(' ENTER YOUR CHOICE : ')
if ord(c) > 48 and ord(c) < 58:
    c = int(c)
else:
    print(' INVALID CHOICE ')
    exit(0)

if c == 1:
    print(' YOU SELECTED 1 i.e.. ARITHMETIC \n')
    x = input(' ENTER AN ARITHMETIC EXPRESSION : ')
    try:
        print(' ANSWER : ', eval(x))
    except NameError:
        print(' YOU ENTERED A WRONG EXPRESSION ')
    except SyntaxError:
        print(' YOU ENTERED A WRONG EXPRESSION ')

elif c == 3:
    print(' 1 : SIN \n 2 : COS \n 3 : TAN \n 4 : COT \n 5 : SEC \n 6 : COSEC \n ')
    z = input(' ENTER YOUR CHOICE : ')
    z = checkisdigit(z)
    trig(z)

elif c == 4:
    print(' YOU SELECTED 4 i.e.. FACTORIAL \n')
    print(' NOTE : ENTER ONLY POSITIVE NUMBER ')
    x = input(' ENTER A VALUE TO GET FACTORIAL : ')
    x = checkisdigit(x)
    try:
        print(factorial(x))
    except RecursionError:
        print(' SORRY , TRY WITH A SMALLER NUMBER WHICH IS LESS THAN 999')
    except ValueError:
        print(' ONLY POSITIVE NUMBERS ARE ALLOWED ')

elif c == 5:
    print(' 1 : SQUARE \n 2 : RECTANGLE \n 3 : RHOMBUS \n 4 : TRIANGLE \n 5 : PARALLELOGRAM \n 6 : CIRCLE')
    x = input(' ENTER YOUR CHOICE : ')
    x = checkisdigit(x)
    if x == 1:
        l1 = input(' ENTER LENGTH OF ONE SIDE OF SQUARE : ')
        l1 = checkisdigit(l1)
        print('AREA OF SQUARE : ', l1*l1)
    elif x == 2:
        l1 = input(' ENTER LENGTH  OF RECTANGLE : ')
        l1 = checkisdigit(l1)
        l2 = input(' ENTER BREADTH OF RECTANGLE : ')
        l2 = checkisdigit(l2)
        print('AREA OF RECTANGLE : ', l1 * l2)
        
    elif x == 3:
        l1 = input(' ENTER BASE OF RHOMBUS : ')
        l1 = checkisdigit(l1)
        l2 = input(' ENTER HEIGHT OF RHOMBUS : ')
        l2 = checkisdigit(l2)
        print('AREA OF RHOMBUS : ', l1 * l2)
        
    elif x == 4:
        l1 = input(' ENTER BASE OF TRIANGLE : ')
        l1 = checkisdigit(l1)
        l2 = input(' ENTER HEIGHT OF TRIANGLE : ')
        l2 = checkisdigit(l2)
        print('AREA OF TRIANGLE : ', ((l1 * l2)//2).__round__(2))
    
    elif x == 5:
        l1 = input(' ENTER LENGTH  OF PARALLELOGRAM : ')
        l1 = checkisdigit(l1)
        l2 = input(' ENTER HEIGHT OF PARALLELOGRAM : ')
        l2 = checkisdigit(l2)
        print('AREA OF PARALLELOGRAM : ', l1 * l2)
        
    elif x == 6:
        l1 = input(' ENTER RADIUS OF THE CIRCLE : ')
        l1 = checkisdigit(l1)
        print('AREA OF CIRCLE : ', (pi * l1 * l1).__round__(2))
    
    else:
        print(' INVALID CHOICE ')

elif c == 6:
    print(' 1 : SQUARE \n 2 : RECTANGLE \n 3 : RHOMBUS \n 4 : TRIANGLE \n 5 : PARALLELOGRAM \n 6 : CIRCLE')
    x = input(' ENTER YOUR CHOICE : ')
    x = checkisdigit(x)
    if x == 1:
        l1 = input(' ENTER LENGTH OF ONE SIDE OF SQUARE : ')
        l1 = checkisdigit(l1)
        print('PERIMETER OF SQUARE : ', 4 * l1)
    elif x == 2:
        l1 = input(' ENTER LENGTH  OF RECTANGLE : ')
        l1 = checkisdigit(l1)
        l2 = input(' ENTER BREADTH OF RECTANGLE : ')
        l2 = checkisdigit(l2)
        print('PERIMETER OF RECTANGLE : ', 2*(l1 + l2))
    elif x == 3:
        l1 = input(' ENTER BASE LENGTH OF RHOMBUS : ')
        l1 = checkisdigit(l1)
        print('PERIMETER OF RHOMBUS : ', l1 * 4)
    elif x == 4:
        l1 = input(' ENTER LENGTH OF SIDE 1 OF TRIANGLE : ')
        l1 = checkisdigit(l1)
        l2 = input(' ENTER LENGTH OF SIDE 2 OF TRIANGLE : ')
        l2 = checkisdigit(l2)
        l3 = input(' ENTER LENGTH OF SIDE 3 OF TRIANGLE : ')
        l3 = checkisdigit(l3)
        print('PERIMETER OF TRIANGLE : ', (l1 + l2 + l3))
    elif x == 5:
        l1 = input(' ENTER LENGTH  OF SIDE 1 OF PARALLELOGRAM : ')
        l1 = checkisdigit(l1)
        l2 = input(' ENTER LENGTH OF SIDE THAT IS ADJACENT TO SIDE 1 OF PARALLELOGRAM : ')
        l2 = checkisdigit(l2)
        print('PERIMETER OF PARALLELOGRAM : ', 2 * (l1 + l2))
    elif x == 6:
        l1 = input(' ENTER RADIUS OF THE CIRCLE : ')
        l1 = checkisdigit(l1)
        print('PERIMETER OF CIRCLE : ', (pi * 2 * l1).__round__(2))
    else:
        print(' INVALID CHOICE ')
        
elif c == 7:
    print(' 1 : BASE 2 LOGARITHM \n 2 : BASE 10 LOGARITHM ')
    s = input(' ENTER YOUR CHOICE : ')
    s = checkisdigit(s)
    logm(s)

elif c == 8:
    print(' YOU SELECTED 8 i.e.. SQUARE ROOT ')
    x = input(' ENTER A POSITIVE NUMBER TO MAKE SQUARE ROOT : ')
    x = checkisdigit(x)
    print(sqrt(x).__round__(2))

else:
    exit(0)

"""
elif c == 2:
    l1 = []
    l2 = []
    m = input(' ENTER ROW SIZE OF FIRST MATRIX : ')
    m = checkisdigit(m)
    n = input(' ENTER ROW SIZE OF FIRST MATRIX : ')
    n = checkisdigit(n)
    p = input(' ENTER ROW SIZE OF SECOND MATRIX : ')
    p = checkisdigit(p)
    q = input(' ENTER ROW SIZE OF SECOND MATRIX : ')
    q = checkisdigit(q)
    print(' 1 : ADDITION \n 2 : MULTIPLICATION ')
    x = input(' ENTER YOUR CHOICE : ')
    x = checkisdigit(x)
    if x == 1:
        if m != p or n != q:
            print(' {}X{} , {}X{} : ADDITION IS NOT POSSIBLE  '.format(m, n, p, q))
            exit(0)
        else:
            print(' ENTER {} VALUES FOR FIRST MATRIX '.format(m * n))
            for i in range(m * n):
                x = input()
                x = checkisdigit(x)
                l1.append(x)
            print(' ENTER {} VALUES FOR SECOND MATRIX '.format(p * q))
            for i in range(p * q):
                x = input()
                x = checkisdigit(x)
                l2.append(x)

            m1 = matrix(l1)
            m2 = matrix(l2)
            m1.resize((m, n))
            m2.resize((p, q))
            print(m1+m2)

    elif x == 2:

        if n != p:
            print(' {}X{} , {}X{} : MULTIPLICATION IS NOT POSSIBLE  '.format(m, n, p, q))
            exit(0)
        else:
            print(' ENTER {} VALUES FOR FIRST MATRIX '.format(m * n))
            for i in range(m * n):
                x = input()
                x = checkisdigit(x)
                l1.append(x)
            print(' ENTER {} VALUES FOR SECOND MATRIX '.format(p * q))
            for i in range(p * q):
                x = input()
                x = checkisdigit(x)
                l2.append(x)

            m1 = matrix(l1)
            m2 = matrix(l2)
            m1.resize((m, n))
            m2.resize((p, q))
            print(m1*m2)

    else:
        print(' INVALID CHOICE ')
"""
