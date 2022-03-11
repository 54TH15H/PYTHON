def fun():
    def lcm(x,y):
        if x>y:
            gt = x
        else:
            gt = y
        while True:
            if gt%x == 0 and gt%y == 0:
                lm = gt
                break
            gt += 1
        return lm


    def gcd(x,y):
        while y:
            x,y = y,x%y
        return x

    # N = int(input())
    lst = []
    # for i in range(N):
    #     lst.append(list(map(int,input().split())))
    lst = [[2,10],[5,15]]
    if len(lst) == 1:
        print(lcm(lst[0][0],lst[0][1]))
        return
    A = []
    B = []
    for i in lst:
        A.append(i[0])
        B.append(i[1])
    temp = [A,B]

    result = []
    for i in range(2):
        n1 = temp[i][0]
        n2 = temp[i][1]
        gd = gcd(n1,n2)
        for j in range(2,len(temp[i])):
            gd = gcd(gd,temp[i][j])

        result.append(gd)
    # print(result)
    print(lcm(result[0], result[1]))





fun()