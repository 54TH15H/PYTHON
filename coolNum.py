def fun():
    def checkRK(n):
        r, k = n.split("  ")
        if int(r)>=1 and int(r)<=105:
            r = int(r)
            if int(k)>=1 and int(k)<=100:
                k = int(k)
                return r,k
            else:
                return checkRK(input())
        else:
            return checkRK(input())

    def decToBin(n):
        rem = 0
        s = ""
        while n>0:
            rem = n%2
            s += str(rem)
            n = n//2
        return s

    count = 0
    R,K = checkRK(input())
    binary = decToBin(R)
    print(binary)
    i = 2
    while i<len(binary):
        if binary[i]=="1":
            if binary[i-2]+binary[i-1]+binary[i] == "101":
                count += 1
                i += 2
            else:
                i+=1
        else:
            i+=1

    print("101 count :",count)
    if count >= K:
        print(1)
    else:
        print(0)
fun()
