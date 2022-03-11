# Palindrome

def fun():
    inp = input('Enter the input : ')
    print('{} is a Palindrome'.format(inp)) if inp == inp[::-1] else print('{} is not a Palindrome'.format(inp))
fun()