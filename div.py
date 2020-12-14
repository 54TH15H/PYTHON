
def checkisdigit(g):
    if g.isdigit():
        return int(g)
    else:
        print(' INVALID ENTRY ')
        exit(0)

def div(a, b):

    c = 0

    try:
        print(' Program Started ')
        c = a // b
        print(c)

    except ZeroDivisionError as z:
        print(" Hey , Plz don't enter zero for second value ")
    finally:
        print(' Program Terminated Successfully ')

x = input(' Enter Numerator Value : ')
x = checkisdigit(x)

y = input(' Enter Denominator Value : ')
y = checkisdigit(y)

div(x, y)
