def fun():
    def mainFun(par):
        retList = []
        for i in range(1,len(par)):
            temp = ''
            for j in range(len(par)):
                if j == i:
                    temp += str(int(par[j])+int(par[j-1]))
                elif j == i-1:
                    pass
                else:
                    temp += str(par[j])
            retList.append(temp)
        return retList

    def listing(lst,n,inp):
        flag = True
        for i in n:
            for j in i:
                if int(j)>2:
                    flag = False
                    break
            if flag:
                lst.append(i)
            else:
                flag = True

    inp = int(input('Enter a Number : '))
    lst = []
    temp = ''
    for i in range(inp):
        temp += '1'
    lst.append(temp)
    length = inp
    while length > 0:
        for i in lst:
            if len(i) == length:
                listing(lst,mainFun(i),inp)

        length -= 1

    lst = list(set(lst))
    print(lst)
    print(len(lst))
fun()
