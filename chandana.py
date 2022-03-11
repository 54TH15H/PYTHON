def fun():
    inp = list(input().split())
    result = 0
    temp = list(set(inp))
    for i in temp:
        if inp.count(i)>1: result += 1
    print(result)




fun()