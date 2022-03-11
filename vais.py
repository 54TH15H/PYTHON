def fun():
    n = int(input())
    inp = list(map(int,input().split()))
    lst1 = []
    lst2 = []
    for i in range(n):
        for j in range(i+1,n):
            lst1.append(inp[i]+inp[j])
            lst2.append(inp[i]*inp[j])
    print(lst1[lst2.index(max(lst2))])
fun()

# 6
# -3 5 -6 9 8 -9