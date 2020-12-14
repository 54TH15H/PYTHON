
# GIVES VALUES UNTIL THE GIVEN NUMBER

def armstrong(n):
    for i in range(1, n+1):
        t = i
        s = 0
        while i > 0:
            r = i % 10
            s = s + r**3
            i = i//10

        if t == s:
            print(t, end='  ')

x = int(input('Enter a number : '))

if x >= 0:
    armstrong(x)
else:
    print('PLZ ENTER A POSITIVE NUMBER')
