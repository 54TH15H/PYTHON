def fact(a=-1):
    if a == 1 or a == 0:
        return 1
    elif a < 0:
        return 'Error'
    else:
        return a*fact(a-1)


print(fact())
