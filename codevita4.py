from itertools import combinations
def fun():
    def prime(inp):
        if inp<2:
            return False
        for i1 in range(2,inp//2 + 1):
            if inp%i1 == 0: return False
        return True

    # n1 = int(input())
    # n2 = int(input())
    n1 = 2
    n2 = 40
    lst = []
    for i in range(n1,n2+1):
        if prime(i): lst.append(i)
    print(lst)
    lst2 = []
    for i in lst:
        for j in lst:
            if i != j and prime(int(str(i)+str(j))): lst2.append(int(str(i)+str(j)))

    print(lst2)
    n1 = lst2[0]
    n2 = lst2[-1]
    c = 0
    n3 = 0
    while c<=len(lst2):
    # while n3 <= 13158006689:
        n3 = n1+n2
        n1 = n2
        n2 = n3
        c += 1
        if n3 == 13158006689:
            break
    print(n3)
    print(c)
    print(len(lst2))
fun()