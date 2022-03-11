def fun():
    def check(lst):
        for j in range(1,len(lst)-1):
            if lst[j] > lst[0]:
                return False
        return True

    N = 9
    A = [5,7,8,7,10,5,2,2,1]
    result = [] # [[5,7],[8,7,10],[]]
    temp = []
    t = []
    i = 0
    while i < N: # 0 1 2 3 4 5
        print(temp)
        if len(temp) <= 1: temp.append(A[i])
        # elif len(temp) == 1: temp.append(A[i])
        else:
            for k in temp:
                t.append(k)
            temp.append(A[i])

            if check(temp):
                if i == N-1:
                    result.append(temp)
                continue
            else:
                result.append(t)
                temp.clear()
                i -= 1
        i += 1

    print(result)
fun()