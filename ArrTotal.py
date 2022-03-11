def fun():

    def checkString(inp):

        if len(inp) > 0 and len(inp) <= 2*10^5:
            return inp
        else:
            print(" Invalid Entry, Try Again ")
            return checkString(input())

    def checkK(inp):

        if int(inp) > 0 and int(inp) <= 10^5:
            return int(inp)
        else:
            print(" Invalid Entry, Try Again ")
            return checkK(input())

    s = checkString(input())
    k = checkK(input())
    count = 0

    for i in range(len(s)):
        try:
            if s[i] != s[i+k]:
                count += 1
        except IndexError:
            print(count)
            exit(0)

fun()