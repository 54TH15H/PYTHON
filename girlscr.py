def fun():
    n = int(input())
    lst = [1,2,3]
    if n<=3 and n>=0:
        print(lst[n-1])
    else:
        for i in range(n-3):
            lst.append(lst[-1]+lst[-2]+lst[-3])
        print(lst[-1])

fun()