# There is a range given n and m in which we have to find the count of all the prime pairs
# whose difference is 6. We have to find how many sets are there within a given range.

# Output:
# The output consists of a single line, print the count prime pairs in a given range. Else print"No
# Prime Pairs".

# Constraints:
# 2<=n<=1000
# n<=m<=2000

# Sample Input:
# 4
# 30

# Output:
# 6

# Explanation:
# (5, 11) (7, 13) (11, 17) (13, 19) (17, 23) (23, 29) . we have 6 prime pairs
# ---------------------------------------------------------------------------------------------------------
def fun():
    def prime(num):
        if num < 2: return False
        for i in range(2,num//2+1):
            if num%i == 0: return False
        return True

    n = int(input())
    m = int(input())
    primes = []
    for i in range(n,m+1):
        if prime(i): primes.append(i)
    result = 0
    for i in primes:
        if prime(i+6): result += 1
    print(result)

fun()