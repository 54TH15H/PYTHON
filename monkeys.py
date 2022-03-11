def  fun():
    n = int(input('No of Monkeys : '))
    k = int(input('Bananas Eatable : '))
    j = int(input('Peanuts Eatable : '))
    m = int(input('No of Bananas : '))
    p = int(input('No of Peanuts : '))
    i = 0
    for i in range(n):
        if m>0: m-=k
        elif p>0: p-=j
        else:
            print(n-i+1)
            break
    if i == n-1:
        print('0 monkeys')

fun()

