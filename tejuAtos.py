# def fun():
#     n = int(input())
#     lst = []
#     for i in range(n): lst.append(int(input()))
#     lst.sort()
#     for i in range(len(lst)-1):
#         if lst[i+1]-lst[i] != 1:
#             print(0)
#             break
#     else: print(1)
# fun()

class UserMainCode(object):
    @classmethod
    def checkConsecutive(cls,input1,input2):
        input2.sort()
        for i in range(input1 - 1):
            if input2[i+1]-input2[i] != 1:
                print(0)
                break
        else: print(1)

n = int(input())
lst = []
for i in range(n): lst.append(int(input()))
UserMainCode.checkConsecutive(n,lst)