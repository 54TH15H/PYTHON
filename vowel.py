def fun():
    n = int(input())
    if n<=0 or n>=10**3:
        exit(0)
    inp = input().lower()
    if len(inp) != n:
        exit(0)
    temp = ''
    for i in inp:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            temp += i
    inp = temp
    result = []
    lst = list(inp)
    lst2 = list(set(lst))
    for i in lst2:
        c=0
        for j in lst:
            if i == j: c+=1
        result.append(c)

    print(lst2[result.index(max(result))])
fun()