def fun():
    inp = int(input())
    if inp <=0 or inp >10**9:
        return
    inpstr = str(inp)
    result = ''

    for i in range(0,len(inpstr),2):
        try:
            result += inpstr[i+1]
            result += inpstr[i]
        except IndexError:
            result += inpstr[i]

    print(result)
fun()