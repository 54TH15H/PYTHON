def fun():
    # def check(n):
    #     if n<1 and n >10**5:
    #         exit(0)
    #     else:
    #         return n

    inp = int(input())
    if inp<2 and inp>10**5: return
    lst = []
    # for i in range(inp): lst.append(check(int(input())))
    for i in range(inp): lst.append(int(input()))

    result = []

    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            print(lst[i],lst[j])
            if lst[i] > lst[j]: break
            else:
                lst.remove(lst[j])
                lst.insert(j,-1)
                break

    for i in lst:
        if i != -1: result.append(i)

    print(result)
fun()

