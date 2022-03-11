mat = [[1,0,0,0,1,0,0],
       [0,0,1,1,0,1,1],
       [1,0,0,0,0,0,1],
       [1,0,0,0,0,0,1],
       [0,0,1,1,0,1,1],
       [0,0,1,1,0,1,1]]

def dicToList(n):
    temp = []
    for i,j in enumerate(n):
        temp.append(n.get(j))

    return temp

def displayMat(n):
    print("\n")
    for i in n:
        for j in i:
            print(j,end="  ")
        print("\n")

def display(n):
    for i in n:
        print(i,end="  ")

def inside(n):
    temp = []
    result = []
    for i in range(1,len(n)-1):
        for j in range(1,len(n[i])-1):
            temp.append(n[i][j])
        result.append(temp)
        temp = []

    return result

def adjFounder(arr,row,col):  # row 1, col 2
    status = {'t':0,'tr':0,'r':0,'dr':0,'d':0,'dl':0,'l':0,'tl':0}
    if row>0:
        if arr[row-1][col] == 1:
            status['t'] = 1
        if col > 0:
            if arr[row-1][col - 1] == 1:
                status['tl'] = 1
        if col < len(arr[row]) - 1:
            if arr[row-1][col + 1] == 1:
                status['tr'] = 1
    if row<len(arr)-1:
        if arr[row+1][col] == 1:
            status['d'] = 1
        if col > 0:
            if arr[row+1][col - 1] == 1:
                status['dl'] = 1
        if col < len(arr[row]) - 1:
            if arr[row + 1][col + 1] == 1:
                status['dr'] = 1
    if col>0:
        if arr[row][col-1] == 1:
            status['l'] = 1
    if col<len(arr[row])-1:
        if arr[row][col+1] == 1:
            status['r'] = 1

    return dicToList(status)

displayMat(mat)
op = inside(mat)
displayMat(op)
print("t  tr r  dr d  dl  l tl")
print('----------------------------------------------------')
for i in range(len(op)):
    for j in range(len(op[i])):
        display(adjFounder(op, i, j))
        print(" -> row:{} column:{} Element:{}".format(i,j,op[i][j]))
