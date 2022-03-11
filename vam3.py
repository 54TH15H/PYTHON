def fun():
    b,f,j,p,v,o = 0,0,0,0,0,0
    for i in input().lower():
        if i == 'b': b += 1
        elif i == 'f': f += 1
        elif i == 'j': j += 1
        elif i == 'p': p += 1
        elif i == 'v': v += 1
        else: o += 1
    if b > 0: print(f'b={b}',end=" ")
    if f > 0: print(f'f={f}',end=" ")
    if j > 0: print(f'j={j}',end=" ")
    if p > 0: print(f'p={p}',end=" ")
    if v > 0: print(f'v={v}',end=" ")
    if o > 0: print(f'others={o}')


fun()