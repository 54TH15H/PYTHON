def fact(n):
    if n < 0:
        print(' Factorial is possible only on positive numbers ')
    else:
        s = 1
        for i in range(1, n+1):
            s *= i
            print(' {}! : {} '.format(i, s))

x = int(input(' Enter a number : '))
fact(x)
