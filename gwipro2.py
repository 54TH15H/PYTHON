def fun():
    n=int(input())
    pro,ind=[],[]
    l=list(map(int,input().split()))
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            l1=[i,j]
            ind.append(l1)
            pro.append(l[i]*l[j])
    v=pro.index(max(pro))
    s=ind[v][0]+ind[v][1]
    print(s)
fun()