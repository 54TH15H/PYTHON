# Given a maximum of four digit to the base 17(10 -> A, 11 -> B, 12 -> C, 16 -> G) as
# input, output its decimal value.

# Input:
# 23GF

# Output:
# 10980
# ------------------------------------------------------------------------------------
def fun():
    b17 = "0123456789ABCDEFG"
    inp = input()[::-1]
    result = 0
    for i in range(len(inp)): result += 17**i*b17.index(inp[i])
    print(result)
fun()