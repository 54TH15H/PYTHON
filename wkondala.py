def fun():
    lst = list("aeiouAEIOU")
    n = int(input())
    result = 0
    for i in input().split():
        if i not in lst: result += 1
    print(result)
fun()