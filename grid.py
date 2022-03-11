def fun():
    def getIndexes(lst):
        temp = []
        for i in range(len(lst)):
            if lst[i] == 'p': temp.append(i)
        return temp

    def numThief(lst2):
        grid = []
        keys = 1
        result = 0
        for i in range(0, len(lst2), 2):
            temp1 = []
            for j in range(lst2[i]):
                temp2 = []
                for k in range(lst2[i]): temp2.append(input())
                temp1.append(temp2)
            grid.append(temp1)

        for i in range(len(grid)):
            result = 0
            for j in range(len(grid[i])):
                temp3 = getIndexes(grid[i][j])
                key = lst2[keys]
                for k in temp3:
                    if k-key >= 0:
                        if grid[i][j][k-key] == 't':
                            result += 1
                            break

                    if k+key < len(grid[i][j]):
                        if grid[i][j][k+key] == 't':
                            result+=1
                            break
            keys += 2
            print(result)

    nt = int(input())
    lst = []
    for i in range(nt):
        n, k = map(int, input().split())
        lst.append(n)
        lst.append(k)
    numThief(lst)
fun()
