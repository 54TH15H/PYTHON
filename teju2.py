# prints n values of fibananci series
def fib(n):
    lst = [0,1]
    if n == 1: print(0)
    elif n == 2: print(*lst)
    else:
        for i in range(n-2): lst.append(lst[-1]+lst[-2])
        print(*lst)

fib(4)
