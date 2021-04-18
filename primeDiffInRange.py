
# MAX DIFFERENCE BETWEEN THE TWO PRIMES IN THE GIVEN RANGE.

def main():

    def checkN(n):
        try:
            n = int(n)
            if n > 0 and n < 11:
                return n
            else:
                raise ValueError
        except ValueError:
            return checkN(input(' ENTER A VALID NUMBER BETWEEN 0 and 11 : '))

    def checkRanges(n):
       try:
           if '  ' not in n:
               print(' INCLUDE 2 SPACES BETWEEN THE NUMBERS , ENTER AGAIN :')
               raise ValueError

           lv, rv = n.split('  ')
           lv = int(lv)
           rv = int(rv)
           if lv >= 2 and rv >= lv and rv <= 10**6:
               return str(lv)+'  '+str(rv)
           else:
               raise ValueError

       except ValueError:
           return checkRanges(input(' INVALID ENTRY, PLZ ENTER AGAIN WITH VALID INPUT [ FOLLOW THE ABOVE NOTE ] : '))


    def prime(n):

        for j in range(2, (n // 2) + 1):
            if n % j == 0:
                return False                # NON-PRIME

        return True                         # PRIME

    def primeInRange(l, r):
        temp = []
        for k in range(l, r + 1):
            if prime(k):
                temp.append(k)

        if len(temp) == 0:
            print(' NO PRIME NUMBERS AVAILABLE IN RANGE ({},{}),HENCE MAXIMUM DIFFERENCE SHOULD BE TAKEN AS -1 '.format(l,r))
        elif len(temp) == 1:
            print(' ONLY ONE PRIME NUMBER AVAILABLE IN RANGE ({},{}),HENCE THE MAXIMUM DIFFERENCE : 0'.format(l,r))
        else:
            print(' MAXIMUM DIFFERENCE IN RANGE ({},{}) : {}'.format(l,r,(temp[-1]-temp[0])))

    T = checkN(input(' ENTER A NUMBER BETWEEN 0 TO 11 : '))
    Range = []

    print(' NOTE : \n\t1. LEFT VALUE SHOULD BE GREATER THAN 1 AND LESS THAN OR EQUAL TO RIGHT VALUE.\n\t2. THE RIGHT VALUE SHOULD BE LESS THAN {}.\n\t3. INCLUDE 2 SPACES BETWEEN THE NUMBERS.'.format(10**6))
    print(' ENTER {} PAIR OF NUMBERS SEPERATED WITH 2 SPACES : '.format(T))

    for i in range(T):
        Range.append(checkRanges(input()))

    for i in range(T):
        L,R = Range[i].split('  ')
        L = int(L)
        R = int(R)
        primeInRange(L,R)

main()
