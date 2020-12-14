
# CHECKS , WEATHER THE GIVEN NUMBER IS ARMSTRONG OR NOT

def armstrong(n):
    t = n
    s = 0
    while n > 0:
        r = n % 10
        s = s+r**3
        n = n//10
    if t == s:
        print('{} IS AN ARMSTRONG NUMBER'.format(t))
    else:
        print('{} IS NOT AN ARMSTRONG NUMBER'.format(t))

x = int(input('Enter a number : '))
if x >= 0:
    armstrong(x)
else:
    print('PLZ ENTER POSITIVE NUMBER')
