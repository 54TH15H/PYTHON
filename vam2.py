def fun():
    inp = input().split(".")
    for i in range(len(inp)):
        if i%2 == 0: print(inp[i],end = ".")
        else: print(inp[i][::-1],end = ".")
fun()