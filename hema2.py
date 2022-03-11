def fun():
    n = int(input())
    fact = 1
    for i in range(1,n+1):
        fact = fact * i

    fact = str(fact)
    n = 0
    for i in fact[::-1]:
        if i == "0":
            n += 1
        else:
            break

    print(n)
   
fun()