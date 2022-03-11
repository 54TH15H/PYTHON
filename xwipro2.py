def fun():
    inp,temp1,temp2 = input(),0,2
    for i in range(0,len(inp)//2):
        if ord(inp[temp1:temp2][0]) < ord(inp[temp1:temp2][1]):print(inp[temp1:temp2][1],end="")
        else:print(inp[temp1:temp2][0], end="")
        temp1,temp2 = temp1+2,temp2+2
    if len(inp)%2 != 0:print(inp[-1])
fun()