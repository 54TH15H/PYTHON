def maxElement(input1):
    count = []
    lst1 = list(input1)
    for i in lst1:
        c = 0
        for j in lst1:
            if i == j: c+=1
        for k in range(c-1): lst1.remove(i)

    for i in lst1:
        c = 0
        for j in list(input1):
            if i == j: c+=1
        count.append(c)
    print(lst1[count.index(max(count))])

input1 = 'aabcdcdba'
maxElement(input1)

