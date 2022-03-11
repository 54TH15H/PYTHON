def fun():

    n = input()
    temp = ''
    for i in n:
        if n.find('EF') >= 0:
            n = n.replace('EF','',2)
        if n.find('56') >= 0:
            n = n.replace('56','',2)
        if n.find('G') >= 0:
            n= n.replace('G','',1)
        if n.find('7') >= 0:
            n= n.replace('7','',1)

    print(n)
fun()
