def fun():
    def isperfect(i):
        for j in range(i//2+1):
            if j*j==i: return True
    n1=int(input())
    n2,l,s=int(input()),[],0
    for i in range(n1,n2+1):
        if isperfect(i):
            l.append(i)
    for i in l: s+=i
    print(s)
fun()