# 1 2 3 4 5
# 5
# 5,4,3,2,1

# 5 - 4 3 2 1
# 4 1 - 3 2
#
# 12 2 3 11 6 8 1
# 1 2 3 6 8 11 12
# 12,11,8,6,3,2,1
def fun():
    # n = int(input())
    # k = int(input())
    a = []
    # a = [4,5,2,1,3]
    a = [12, 11, 8, 6, 3, 2, 1]
    b = list(a)
    # for i in range(n):
    #     a.append(int(input()))
    a.sort()
    b.sort()
    a.reverse()
    print(a)
    print(b)
    count = 1
    result = []
    for i in a:
        temp2 = [i]
        if i+a[-count] <= 12:
            temp2.append(a[-count])
            count += 1
        temp2.sort()
        result.append(temp2)

    
    print(result)



fun()

