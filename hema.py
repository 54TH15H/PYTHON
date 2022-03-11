# def fun():
#     def countSubarr(arr, n):
#         um = dict()
#         curr_sum, count = 0,0
#         for i in range(n):
#             curr_sum += (-1 if (arr[i] == 0) else arr[i])
#             if um.get(curr_sum):
#                 um[curr_sum] += 1
#             else:
#                 um[curr_sum] = 1
#         for itr in um:
#             if um[itr] > 1:
#                 count += ((um[itr] * int(um[itr] - 1)) / 2)
#         if um.get(0): count += um[0]
#         return int(count)
#     n = int(input())
#     arr = []
#     for i in range(n):
#         arr.append(int(input()))
#     print(countSubarr(arr, n))
# fun()
class UserMainCode(object):
    @classmethod
    def largestSubarray(cls,input1,input2):
        um = dict()
        curr_sum, count = 0, 0
        for i in range(input1):
            curr_sum += (-1 if (input2[i] == 0) else input2[i])
            if um.get(curr_sum):
                um[curr_sum] += 1
            else:
                um[curr_sum] = 1
        for itr in um:
            if um[itr] > 1:
                count += ((um[itr] * int(um[itr] - 1)) / 2)
        if um.get(0): count += um[0]
        return int(count)
obj = UserMainCode()
try:
    n = int(input())
except EOFError:
    exit(0)
arr = []
for i in range(n):
    arr.append(int(input()))
print(obj.largestSubarray(n,arr))