def fun():
    n = int(input())
    lst = list(input().split(' '))
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    temp2 = []
    for i in range(1,2**n):
        temp = list(bin(i)[2:])
        while len(temp) < 4:
            temp.insert(0,'0')
        temp2.append(temp)
    result = []
    for i in temp2:
        s = 1
        for j in range(len(i)):
            if i[j] == '1':
                s *= lst[j]
        if s<0:
            result.append(s)

    # print(len(result))

    if len(result):
        print(len(result))
    else:
        print(-1)
fun()