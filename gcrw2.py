def fun():
    n = int(input())
    lst = []
    for i in input().split():
        lst.append(int(i))
    lst.sort()
    if n%2 == 0: print(lst[n//2]+lst[n//2-1])
    else: print(lst[n//2])
fun()