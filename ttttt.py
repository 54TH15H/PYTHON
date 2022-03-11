def func(s):
    for i in s:
        if i>=1 and i<=10**9:
            b.append(i)
        return b
def fun2(a):
    for i in range(N,2):
        sum2=a[i]+a[i+1]
        sum1.append(sum2)
    print(sum1)
    value=max(sum1)-min(sum1)
    print("value is",value)

N=int(input())
s=[]
b=[]
a=[]
sum1=[]
sum2=0
for i in range(N):
    s.append(int(input()))
if N%2==0 and N>=1 and N<=200000:
    b=func(s)
if b:
    fun2(b)