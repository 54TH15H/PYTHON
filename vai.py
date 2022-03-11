def fun():
    n = int(input())
    inp = input()
    s = 0
    for i in inp.split():
        if int(i) > 0: s +=  int(i)
    print(s)
fun()