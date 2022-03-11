# from itertools import permutations
# def fun():
#     n = int(input())
#     m = int(input())
#     lst = []
#     for i in list(permutations(str(m))): lst.append(int("".join(list(i))))
#     lst.sort()
#     print(lst[lst.index(m)+1])
# fun()


from itertools import permutations
class UserMainCode(object):
    @classmethod
    def nextGreater(cls, input1, input2):
        lst = []
        for i in list(permutations(str(input2))): lst.append(int("".join(list(i))))
        lst.sort()
        print(lst[lst.index(input2)+1])

n = int(input())
m = int(input())
UserMainCode.nextGreater(n, m)