def fun():

    def checkN(n):

        if int(n) > 0  and int(n) <= 10**5:
            return int(n)
        else:
            return checkN(input())

    def checkInp(n):

        if int(n) > 0  and int(n) <= 1000:
            return int(n)
        else:
            print(' Invalid Entry,Try again ')
            return checkInp(input())

    size = checkN(input())
    lst = []
    for i in range(size):
        lst.append(checkInp(input()))

    lst.sort()
    totalSum = sum(lst)

    for i in range(1,max(lst)+1):
        if size*i <= totalSum:
            continue
        else:
            print(i)
            exit()

fun()

