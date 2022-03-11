# print prime numbers until the given number
def prime(n):
    for i in range(2,n+1):
        j = 0
        for j in range(2,i//2+1):
            if i%2 == 0: break
        else: print(i,end=" ")
prime(10)