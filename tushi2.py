def solve(s):
    inp = list(s)
    inp.sort()
    temp = list("doselect")
    temp.sort()
    if "".join(inp).index("".join(temp)) != -1: return "NO"
    else: return "YES"















# def fun():
#     # inp = list(input())
#     inp = "dddecttdoselect"
#     temp = list("doselect")
#     dic1 = {}
#     for i in inp:
#         if i not in dic1.keys(): dic1[i] = 1
#         else: dic1[i] += 1
#     print(dic1)
#     dic2 = {}
#     for i in temp:
#         if i not in dic2.keys(): dic2[i] = 1
#         else: dic2[i] += 1
#     print(dic2)
# fun()
