def fun():
    # s = input().lower()
    # if len(s)<1 or len(s)>10**5:
    #     return
    # k = int(input())
    # if k<1 or k>10**3:
    #     return
    ss = "zzzzza"
    s = "zzzazz"
    k = 2
    result = ''
    print(list(s))
    s = list(s)
    s.sort()
    s.reverse()
    print(s)
    for i in range(len(s)):
        print(ss[i:i+k+1])





fun()
