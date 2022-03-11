def fun():
    # 0 0 0 0 0 0
    # 0 0 0 1 1 0
    # 0 1 1 1 0 0
    # 1 1 1 1 0 1
    #
    #

    # inp = input().split(":")
    inp = "13:37:41".split(":")
    lst = []
    for i in inp:
        for j in range(2):
            temp = bin(int(i[j]))[2:]
            while len(temp) < 4:
                temp = "0" + temp
            lst.append(list(temp))
    print(lst)
fun()