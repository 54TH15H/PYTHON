# DECIMAL NUMBER TO BINARY CONVERSION.

def dToB():
    def check(n):

        try:
            if int(n) >= 0:
                return int(n)
            else:
                raise ValueError
        except ValueError:
            return check(input(' ENTER A POSITIVE NUMBER : '))

    inp = check(input(' ENTER A POSITIVE NUMBER : '))
    lst = []

    if inp == 0:
        print(' BINARY FORMAT : 0 ')
    else:
        while inp > 0:
            lst.append(inp % 2)
            inp = inp // 2

        print(' BINARY FORMAT : ', end='')
        lst.reverse()
        for i in lst:
            print(i, end=' ')

dToB()

