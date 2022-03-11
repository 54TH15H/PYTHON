def fun():
    inp = input()
    l,r = 0,0
    for i in inp:
        if i == "{":
            l += 1
        elif i == "}":
            r += 1
    if l == r:
        print("correct")
    else:
        print("error")
fun()