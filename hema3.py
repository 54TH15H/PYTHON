def getDecreasing():
    def check(n):
        temp = n[0]
        for j in range(1,len(n)):
            if temp>=n[j]:
                temp = n[j]
                if j == len(n)-1:
                    return True
                continue
            else:
                return False
        else:
            return True

    N = int(input())
    count = 0
    for i in range(N+1):
        if check(str(i)): count += 1
    print(count)

getDecreasing()