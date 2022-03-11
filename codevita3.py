def fun():
    def prime(inp):
        if inp<=1: return False
        for i in range(2,inp//2+1):
            if inp%i == 0: return False
        return True

    # n = int(input())
    n = 20
    c = 0
    lst = []
    for j in range(2,n+1):
        if prime(j): lst.append(j)
    print(lst)
    if len(lst)<3:print(0)
    else:
        s = lst[0]
        for k in range(1,len(lst)):
            s += lst[k]
            if s in lst:
                c += 1
    print(c)


fun()