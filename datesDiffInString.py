# PROGRAM TO IDENTIFY THE DIFFERENCE BETWEEN THE TWO DATES PRESENT IN THE INPUT STATEMENT.
# THE DATES MUST BE REAL AND IN THE FORMAT OF DD:MM:YYYY.

def fun():

    def checkMonth(d,m,y):

        if y % 4 == 0:
            dic = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        else:
            dic = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        if d > 0 and d <= dic[m]:
            return True
        else:
            return False

    def checkDate(n):

        dd = int(inp[n] + inp[n + 1])
        mm = int(inp[n+3] + inp[n+4])
        yy = int(inp[n + 6] + inp[n + 7] + inp[n + 8] + inp[n + 9])

        if mm > 0 and mm < 13 and checkMonth(dd,mm,yy):
            return True
        else:
            return False

    def checkDFormat(n):

        try:
            if inp[n + 1].isdigit and inp[n + 2].isalpha and inp[n + 3].isdigit and inp[n + 4].isdigit and inp[
                n + 5].isalpha and inp[n + 6].isdigit and inp[n + 7].isdigit and inp[n + 8].isdigit and inp[
                n + 9].isdigit:
                if inp[n + 2] == inp[n + 5] and checkDate(n):
                    date.append(inp[n:n + 10])
                    print(date)
                    return n + 10

                else:
                    return n + 1

        except IndexError:
            return len(inp)+1

    inp = input(" ENTER ANY STATEMENT THAT CONSISTS OF TWO DATES IN THE FORMAT OF DD:MM:YYYY :\n")
    date = []
    i = 0
    
    while i < len(inp):
        
        if inp[i].isalpha() or inp[i] == ' ':
            i += 1
            continue
        else:
            i = checkDFormat(i)

    j = 0
    if len(date) == 0:
        print(' NO DATES IN THE INPUT STATEMENT. ')
    elif len(date) == 1:
        print(" ONLY ONE DATE FOUND '{}' , NO WAY TO FIND THE DIFFERENCE.".format(date[0]))
    else:
        print('DIFFERENCE BETWEEN {} AND {} : {}.'.format(date[0][6:],date[1][6:],abs(int(date[0][6:])-int(date[1][6:]))))

fun()