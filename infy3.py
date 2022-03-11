def fun():
    inp = "xxyyzz"
    t = []
    for i in range(2**len(inp)):
        # print(i)
        binary = bin(i)[2:]
        s = "0"
        for i in range(len(inp)-len(binary)):
            binary = s + binary
        if binary.count('1') == 2:
            # print("({},{})".format(binary.find('1')+1, binary.find('1', binary.find('1') + 2)))
            t.append([binary.find('1')+1, binary.find('1', binary.find('1') + 2)])

    c = 0
    for i in t:
        if i[0] != -1 and i[1] != -1:
            c += 1

    if c%2 == 0:
        print(c)
    else:
        print(c-1)

fun()