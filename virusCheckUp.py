
def main():
    # Write code here

    def checkN(n):

        try:
            n = int(n)
            if n > 0 and n < 11:
                return n
            else:
                raise ValueError

        except ValueError:
            return checkN(input('INVALID ENTRY,FOLLOW THE NOTE AND ENTER AGAIN : '))

    def checkCompVirus(comp):
        if len(comp) > 0 and len(comp) <= 10 ** 5:
            return comp.lower()
        else:
            return checkCompVirus(input(' ENTER THE DNA COMPOSITION WHOSE LENGTH IS IN BETWEEN {} AND {} : '.format(0, 10 ** 5)))

    def checkCompPatient(comp):
        if len(comp) > 0 and len(comp) <= len(Virus):
            return comp.lower()
        else:
            return checkCompPatient(input('INVALID ENTRY,FOLLOW THE NOTE AND ENTER AGAIN : '))

    print(' NOTE : THE DNA COMPOSITION LENGTH SHOULD BE IN BETWEEN {} AND {} : '.format(0, 10 ** 5))
    Virus = checkCompVirus(input(' Enter the Virus composition : '))

    print(' NOTE : PATIENTS COUNT SHOULD BE GREATER THAN 0 AND LESS THAN 11 ')
    N = checkN(input(' Enter count of the People Available for the test : '))

    bList = []
    print(' NOTE : PATIENTS DNA COMPOSITION LENGTH SHOULD BE IN BETWEEN {} AND {} : '.format(0, len(Virus)+1))
    print(' ENTER THE BLOOD COMPOSITIONS OF {} PEOPLE : '.format(N))
    for i in range(N):
        bList.append(checkCompPatient(input()))

    for a in bList:

        t = Virus
        for i in a:
            for j in t:
                if i == j:
                    a = a.replace(i, '', 1)
                    t = t.replace(j, '', 1)
                    break
                else:
                    t = t.replace(j, '', 1)

        if t == a or len(a) == 0:
            print(' POSITIVE ')
        else:
            print(' NEGATIVE ')

main()

