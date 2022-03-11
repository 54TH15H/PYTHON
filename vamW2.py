def fun():
    n ,lst= int(input()),list(map(int,input().split(" ")))
    lst.sort()
    if len(lst)%2 == 0:print(f'{lst[len(lst)//2-1]+lst[len(lst)//2]}')
    else:print(lst[len(lst)//2])
fun()