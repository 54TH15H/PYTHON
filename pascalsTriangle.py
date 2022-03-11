def fun():
    def check(n):
        try:
            return int(n)
        except ValueError:
            print('Invalid input, Please enter a Number : ',end = '')
            return check(input())

    inp = check(input('Enter the height of the pascal\'s triangle : '))
    temp = [0,1,0]
    for i in range(1,inp+1):
        lst = [0]
        for j in range(1,i+1):
            lst.append(temp[j]+temp[j-1])
        temp = lst
        temp.append(0)

        for k in range(inp-i):
            print(' ',end='')
        for k in range(1,len(temp)-1):
            print(temp[k],end=' ')
        print('\n')

fun()