# Your code here
def func():
    def checkSize(n):

        if int(n) > 0 and int(n) <= 100000:
            return int(n)
        else:
            return checkSize(input())

    def checkInp(n):

        if int(n) > 0 and int(n) <= 10 ** 15:
            return int(n)
        else:
            return checkInp(input())

    size = checkSize(input)
    lst = []
    for i in range(size):
        lst.append(checkInp(input()))

    start = lst[0]
    count = 1
    for i in range(1, len(lst)):
        if start < lst[i]:
            count += 1
            start = lst[i]

    print(count)

func()