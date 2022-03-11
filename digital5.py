# One programming language has the following keywords that cannot be used as
# identifiers:
# break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct,
# type, var
# Write a program to find if the given word is a keyword or not

# Input 1:
# defer
# Output:
# defer is a keyword

# Input 2:
# While
# Output:
# while is not a keyword
# -------------------------------------------------------------------------------------
def fun():
    lst = "break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct, type, var".split(", ")
    inp = input()
    if inp in lst: print(f'{inp} is a keyword')
    else: print(f'{inp} is not a keyword')
fun()