# swapping two values without using third variable
def swap():
    n1,n2 = 2,4
    n1 = n1+n2
    n2 = n1-n2
    n1 = n1-n2
    print(n1,n2)

swap()