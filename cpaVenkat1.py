import string


def fun():
    n = int(input())
    inp = input()[0]
    special = list("[@_!#$%^&*()<>?/\|}{~:]`-+=;.,")
    v = list("AEIOUaeiou")
    lst = []
    for i in range(n): lst.append(input())
    if inp not in special:
        print("Not a Special Character" )
        exit(0)
    result = []
    for i in lst:
        temp = ""
        for j in i:
            if j in v: temp += inp
            else: temp += j
        result.append(temp)
    for i in result: print(f'{i} {i.count(inp)}')
fun()