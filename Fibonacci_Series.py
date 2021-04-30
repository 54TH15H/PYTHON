def check(n):
    try:
        if int(n) < 0:
            raise ValueError
        else:
            return int(n)
    except ValueError:
        print("Invalid input")
        return check(input("Plz, Enter a Valid Number : ))

print(" Fibonacci Series ")
a, b = 0, 1
num = check(input("Enter a Positive Number : "))
if num == 0:
    print("   ")
elif num == 1:
    print("0")
elif num == 2:
    print("0  1")
else:
    print(a, end = "  ")
    print(b, end = "  ")
    for i in range(2, num):
        c = a+b
        print(c, end = "  ")
        a, b = b, c
