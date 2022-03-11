# 5 4 2
#
# 1 - 1 1 1 - 4 3 1
# 2 - 1 1 1 - 3 2 0
# 3 - 2 1 0 - 1 1 0
#

def fun():
    m = int(input())
    n = int(input())
    p = int(input())
    if m<0 or m>1000 or n<0 or n>1000 or p<0 or p>1000:
        return
    print((m+n+p)//3)

fun()