def fun():
    ini=int(input())
    temp=ini
    f=int(input())
    n=int(input())
    l=[]
    l.append(temp)
    for i in range(n-1):
        temp+=f
        l.append(temp)
    for i in l:
        print(i,end=" ")
fun()