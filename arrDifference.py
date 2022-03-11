
def FindCount(a ,l , n ,d):

    count = 0
    for i in a:
        if abs(n - i) <= d :
            count += 1

    if count == 0:
        return -1
    else:
        return count

arr = [16, 3, 17, 56, 77, 100]
num = 13
diff = 2

print(FindCount(arr,len(arr),num,diff))