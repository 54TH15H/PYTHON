def fun():
    n1 ,lst1= int(input()),list(map(str,input().split()))
    n2 ,lst2= int(input()),list(map(int,input().split()))
    for i in range(n1):print(f'{lst1[i]} {lst2[i]}',end=" ")
fun()