def numToChar(q):
    def getChar(n):
        return chr(n+64)

    result ,temp= [],''
    if q>0 and q<27:
        print(getChar(q))
        return

    while q>26:
        r, q = q%26, q//26
        if r == 0: r, q = r+26, q-1
        result.insert(0,r)
    result.insert(0,q)

    for i in result: temp += getChar(i)
    print(temp)

for i in range(1,10000):
    print(i,end='  ')
    numToChar(i)

# def charToNum(n):
#     l = len(n)
#     total = 0
#     for i in range(l):
#         total += 26**i*charNum(n[-1-i])
#     return total
#
# def charNum(n):
#     return ord(n) - 64