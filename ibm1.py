def fun(lst):
    # n = int(input())
    # lst = []
    # for i in range(n):
    #     inp = int(input())
    #     if inp >= 0 and inp not in lst:
    #         lst.append(inp)
    #     else:
    #         exit()
    result = []
    lst1 = []
    lst2 = []
    lst.sort()
    for i in range(len(lst)//2):lst1.append(lst[i])
    for i in range(-1,-((len(lst)//2)+2),-1): lst2.append(lst[i])

    for i in range(len(lst2)):
        try:
            result.append(lst2[i])
            result.append(lst1[i])
        except Exception:
            break

    if len(lst) % 2 == 0:
        print(result[:len(lst)])
    else:
        print(result)


numbers = [6,8,5,4,9,7,2,1,3]
fun(numbers)
