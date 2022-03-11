def fun():
    n = int(input())
    lst = list(map(int,input().split()))
    result = 0
    for i in lst:
        if i>0: result += i
    print(result)


fun()