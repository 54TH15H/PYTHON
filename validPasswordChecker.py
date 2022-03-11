
def fun(n):
    numericDigit = False
    capitalLetter = False
    spaceSlash = True

    for i in n:

        if i.isnumeric():
            numericDigit = True

        if i.isupper():
            capitalLetter = True

        if i == ' ' or i == '/':
            spaceSlash = False

    if len(n) >= 4 and numericDigit and capitalLetter and spaceSlash and n[0].isnumeric != True :
        print(1)
    else:
        print(0)

inp = input('Enter a Password : ')
fun(inp)

