# CHECKING WHETHER THE GIVEN INPUT IS PRIME OR NON-PRIME NUMBER 

def check(y):
    try:
        return abs(int(y))
    except ValueError:
        print(" YOU ENTERED A NON-INTEGER , PLZ ENTER AGAIN :")
        return check(input())

def prime(v):                     # 1 : NON-PRIME OR COMPOSITE
                                  # 0 : PRIME NUMBER
    if v==0 or v==1 :
        return 1
    else:
        for i in range(2,(v//2)+1):
            if v%i==0:
                return 1
            else:
                continue
        else:
            return 0

n = check(input(" ENTER A NUMBER : "))
if prime(n):
    print(" {} IS A COMPOSITE NUMBER ".format(n))
else:
    print(" {} IS A PRIME NUMBER ".format(n))

