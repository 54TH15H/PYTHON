
def flames(a, b):
    c = 0
    l1 = list(set(a))
    l2 = list(set(b))
    l1.sort()
    l2.sort()
    for i in l1:
        for j in l2:
            if i == j:
                l1.remove(i)
                l2.remove(j)
                break
    for i in l1:
        c += 1
    for i in l2:
        c += 1
    return c


def output(n):
    if n == 1:
        print('SOMETHING')
    elif n == 2 or n == 4 or n == 7 or n == 9:
        print('ENEMIES')
    elif n == 3 or n == 5:
        print('FRIENDS')
    elif n == 6:
        print('MARRIAGE')
    elif n == 8:
        print('ATTRACTION')
    elif n == 10:
        print('LOVE')
    else:
        print("PROGRAM'S CAPACITY IS COMPLETED")

x = input('Enter First name : ')
y = input('Enter Second name : ')
output(flames(x, y))
