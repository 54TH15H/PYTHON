def fib(n):
    if n < 0:
        print(' Fibonacci series is possible only on positive numbers ')
    elif n == 0:
        print('None')
    elif n == 1:
        print(0)
    else:
        print('First {} numbers in Fibanansi series : '.format(n))
        a = 0
        b = 1
        print(a, end=' ')
        print(b, end=' ')
        for i in range(2, n):
            s = a+b
            a = b
            b = s
            print(s, end=' ')


x = int(input(' Enter a number : '))
fib(x)
