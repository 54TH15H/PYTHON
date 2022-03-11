def fun():
    n = int(input())
    lst = list(map(int,input().split()))
    m = int(input())
    lst.sort()
    print(lst[-m])

fun()