# factorial of m natural numbers
def fact(n):
    if n <= 1: return 1
    return n*fact(n-1)
m = 5
for i in range(1,m+1):
    print(fact(i),end=" ")