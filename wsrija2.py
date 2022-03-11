def fun():
    n = int(input())
    n1 = int(input())
    n2 = int(input())
    lst = []
    for i in range(1,max(n//n1,n//n2)+1):
        if i*n1 <= n:
            if i*n1 not in lst: lst.append(i*n1)
        if i*n2 <= n:
            if i*n2 not in lst: lst.append(i*n2)
    print(sum(lst))

fun()