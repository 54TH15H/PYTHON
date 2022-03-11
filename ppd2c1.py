from itertools import combinations
def fun():
    # N = int(input())
    # lst = []
    # for i in range(N):
    #     lst.append([input(),input()])
    lst = [["babbcd","accbce"],["abbccdde","ccbd"],["subs","sub"]]
    sub = []
    for i in lst: sub.append([i[0][j:k] for j in range(len(i[0])) for k in range(j+1,len(i[0])+1) if len(i[0][j:k]) == len(i[1])])
    res = []
    for i in range(len(lst)):
        res.append([])
        for j in sub[i]:
            c = 0
            for l in range(len(j)):
                if j[l] != lst[i][1][l]: c += 1
            res[i].append(c)
    for i in res: print(min(i))
fun()