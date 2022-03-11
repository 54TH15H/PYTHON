from itertools import permutations
def fun():
    # n = int(input())
    # lst = []
    # for i in range(n): lst.append(int(input()))
    # ------------------------------------------------------------------------------
    n = 10
    lst = [3,4,5,-3,100,1,89,54,23,20]
    # ------------------------------------------------------------------------------
    # n = 8
    # lst = [4,-45,5,132,46,77,-12,3]
    # ------------------------------------------------------------------------------
    s = ""
    for i in range(n//2): s += '10' #10101010
    perm = []
    for i in permutations(s):perm.append(list(i))
    perm2 = []
    for i in perm:
        if i not in perm2: perm2.append(i)
    result = []
    for i in perm2:
        l ,r = 0 ,0
        for j in range(len(i)):
            if i[j] == '1': l += int(lst[j])
            else: r += int(lst[j])
        result.append(abs(l-r))
    print(min(result))

fun()