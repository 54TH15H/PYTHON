n = int(input())
lst = list(map(int,input().split()))[::-1]
s = 0
for i in range(len(lst)//2): s += lst[i]
print(s)
