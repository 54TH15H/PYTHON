
# PROGRAM TO FIND FIBONACCI SERIES UNTIL A GIVEN NUMBER
def fib(n):
    if n < 0:
        print(' Fibonacci series is possible only on positive numbers ')
    elif n == 0:
        print(0)
    else:
        a = 0
        b = 1
        print(a, end=' ')
        print(b, end=' ')
        s = a+b
        while s <= n:
            a = b
            b = s
            print(s, end=' ')
            s = a+b

x = int(input(' Enter a number : '))
fib(x)
