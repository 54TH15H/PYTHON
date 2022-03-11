# def getList(n):
#     lst1 = [10,50,100,500,1000]
#     for i in range(1,len(lst1)):
#         if n > lst1[i-1] and n < lst1[i]:
#             return lst1[i-1],lst1[i]
#
#
# def intialList(n):
#     temp = []
#     n = list(str(n)[::-1])
#     for i in range(len(n) - 1, -1, -1):  # 2 1 0
#         temp.append(int(n[i]) * 10 ** i)
#     while 0 in temp:
#         temp.remove(0)
#     return temp
#
# for i in range(1,1000):
#     print(intialList(i))
# 300 = [100,500]
# if 300%100 <= 3:
#     for i in range(300%100):
#         re
# print(intialList(160))
# print(getList(70))
# print(60//50)
#
#

# def getList(n):
#     temp = []
#     n = list(str(n)[::-1])  # 9 7 1
#     print(n)
#     for i in range(len(n) - 1, -1, -1): temp.append(int(n[i]) * 10 ** i)
#     while 0 in temp: temp.remove(0)
#     return temp
#
# print(getList(10))

def fun(n):
    lst1 = [10, 50, 100, 500, 1000]
    temp = []
    for i in range(1,len(lst1)):
        if n > lst1[i-1] and n < lst1[i]:
            temp.append(lst1[i-1])
            temp.append(lst1[i])
    if temp[1] not in lst1:
        temp1 = fun(temp[1])

    return temp
fun(70)
