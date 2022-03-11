def fun():
    lst = [[1],[2,3],[4,5,6],[7,8,9,10]]
    c = 0
    for i in lst:
        print("\n")
        print(i,end="\n\n")
        l = len(i)
        temp = []
        temp1 = []
        for j in range(2**l):
            s = bin(j)[2:]
            while len(s) < l:
                s = '0'+s
            print(s,end=' ')

            temp2 = ''
            p = 1
            for k in range(len(s)):
                if s[k] == '1':
                    p = p * int(i[k])
                    temp2 = str(p)
            if temp2:
                print(' : '+temp2)
            else:
                print(' : 0')

fun()