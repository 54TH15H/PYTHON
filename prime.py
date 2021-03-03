def check(t):
    try:
        return abs(int(t))
    except ValueError:
        print(" YOU ENTERED A NON-INTEGER , PLZ TRY AGAIN : ")
        return check(input())

def prime(v):                 # 1: NON-PRIME
                              # 0: PRIME
    if v == 0 or v == 1:
        return 1
    else:
        for i in range(2, (v // 2) + 1):
            if v % i == 0:
                return 1
            else:
                continue
        else:
            return 0

n = check(input(" ENTER A NUMBER : "))
for k in range(2,n+1):
    if prime(k):
        continue
    else:
        print(k,end="  ")

