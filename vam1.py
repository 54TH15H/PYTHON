def fun():
    inp = input()
    dic = {}
    for i in inp:
        if i in dic.keys(): dic[i] += 1
        else: dic[i] = 1
    print(dic)




fun()