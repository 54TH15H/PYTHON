# Write a program to print all the combinations of the given word with or without meaning
# (when unique characters are given).

# Sample Input:
# abc

# Output:
# abc
# acb
# bac
# bca
# cba
# cab
# ------------------------------------------------------------------------------
from itertools import permutations
def fun():
    # inp = list(input())
    inp = "abc"
    for i in list(permutations(inp)): print("".join(i))
fun()