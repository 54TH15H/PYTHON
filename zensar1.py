def fun():
    def isPrime(n):
        if n<2:return False
        for i in range(2,n//2+1):
            if n%i == 0: return False
        return True
    def check(n):
        while len(n) > 1:
            n = list(n)
            s = 0
            for i in n: s += int(i)
            n = str(s)
        return isPrime(int(n))

    l , r = map(int,input().split(" "))
    prime = []
    for i in range(l,r+1):
        if isPrime(i): prime.append(str(i))
    for i in prime:
        if check(i):print(i,end=" ")
fun()
