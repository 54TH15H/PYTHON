def fun():
    l = 109
    r = 120
    # --------------------------------------------------------------------
    # l = int(input())
    # r = int(input())
    # --------------------------------------------------------------------
    c = 0
    for i in range(l,r+1):
        if len(list(str(i))) == len(list(set(list(str(i))))): c += 1
    print(c)
fun()