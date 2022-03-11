def fun():

    def checkBCount(inp):
        if int(inp) > 0 and int(inp) <= 100:
            return int(inp)
        else:
            print('INVALID ENTRY ,Try Again')
            return checkBCount(input())

    def checkCapacity(inp):
        if int(inp) > 0 and int(inp) <= 50:
            return int(inp)
        else:
            print('INVALID ENTRY ,Try Again')
            return checkBCount(input())

    def checkInput(inp):
        if int(inp) >= 0 and int(inp) <= c:
            return int(inp)
        else:
            print(" Invalid Entry ,Try Again")
            return checkInput(input())

    def checkPair(a, b ,d):

        if a != 0 and b != c:
            d += 1
            return d                # 8 0 0 10      22
        elif a != c and b != 0:     # 10 8 0 0
            d +=1
            return d
        else:
            return d

    n = checkBCount(input(' NUM OF BOTTLES : '))    # no of bottles
    c = checkCapacity(input(' CAPACITY '))
    count = 0
    lst = []
    bc = []
    for i in range(n):
        bc.append(checkInput(input()))

    for i in range(len(bc)):
        try:
            count = checkPair(bc[i],bc[i+1],count)
        except IndexError:
            print(count)

fun()

