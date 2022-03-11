def fun():
    n = int(input())
    if n>=2 and n<=1000:
        arr = []
        result = []
        for i in range(n):
            arr.append(int(input()))

        for i in range(n):
            for j in range(n):
                if i!=j:
                    result.append(abs(arr[i]-arr[j]))

        print(min(result))
fun()
