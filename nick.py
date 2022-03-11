def checkConsecutive(input1,input2):
    input2.sort()
    i = 0
    for i in range(1,input1):
        if input2[i]-input2[i-1] != 1:break

    if i == input1-1:
        return 1
    return 0

input1 = 6
input2 = [3,7,2,5,4,6]
print(checkConsecutive(input1,input2))