def solve():
    a = [6,7,9]
    b = [5,2,9]
    # a = [1,2,3,4]
    # b = [1,1,1,4]
    # if N == 1: return 2099828
    # if N == 3: return 615902705

    temp = 0
    ts = len(a)
    result = []
    while ts > 0:
        for i in range(len(a)-1,-1,-1):
            tm = a[i]
            # if temp == len(b): temp = 0
            if temp == len(b):
                ts = 0
                break
            if tm >= b[temp]:
                result.append(a.index(tm)+1)
                # print(a.index(tm)+1)
                a.remove(tm)
                a.insert(0,tm)
                break

        temp += 1
        ts -= 1

    print(result)
    rr = result[::-1]
    r = 10**5 + 3
    fr = 0
    for i in range(len(rr)):
        fr += rr[i]*(r**i)



    print( fr%(10**9 + 7))

solve()
