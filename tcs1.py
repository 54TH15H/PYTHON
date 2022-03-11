def fun():
    l = int(input())
    r = int(input())
    result = 0
    for i in range(l,r+1):
        result += i*len(str(i))

    print(result)

fun()