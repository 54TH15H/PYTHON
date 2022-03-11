def fun():
    s = 0
    for i in input():
        if int(i)%2 != 0: s += int(i)
    print(s)

fun()