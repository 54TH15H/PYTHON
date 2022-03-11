def fun():
    def prime(n):
        if n<=1: return False
        for i in range(2,n//2+1):
            if n%i == 0:return False
        else:
            return True
    result = 0
    for i in input():
        if prime(int(i)): result += int(i)
    print(result)
fun()