def fact(n):
    if n < 0:
        print('Factorial is possible only on positive numbers')
        return None
    else:
        s = 1
        for i in range(1, n+1):
            s = s*i
        return s

x = int(input(' Enter a number : '))
print(' {}! : {} '.format(x, fact(x)))
