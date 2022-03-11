def fun():
    inp1 = input()
    inp2 = input()
    for i in range(max(len(inp1),len(inp2))):
        try:
            if inp1[i] != inp2[i]:
                if len(inp1) > len(inp2):
                    print(inp1[i])
                else:
                    print(inp2[i])
                return
        except IndexError:
            if len(inp1) > len(inp2):
                print(inp1[i])
            else:
                print(inp2[i])
            return

fun()