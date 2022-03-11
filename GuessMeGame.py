
#  GUESS ME GAME
import random


def check(n):
    try:
        if int(n) == 1 or int(n) == 2:
            return int(n)
        raise ValueError
    except ValueError:
        print(' INVALID CHOICE ')
        print(' \t1 : Yes ')
        print(' \t2 : No ')
        return check(input(' ENTER A VALID CHOICE : '))

def checkChoice(n):
    try:
        if int(n) > 0 or int(n) < 21:
            return int(n)
        raise ValueError
    except ValueError:
        return checkChoice(input(' INVALID CHOICE , FOLLOW THE NOTE AND ENTER THE INPUT AGAIN : '))

def fun():
    num = checkChoice(input())



userName = input(' PLEASE ENTER YOUR NAME : ')
print(' WELCOME ',userName.upper())

print(' SHALL WE BEGIN? ')
print(' \t1 : Yes ')
print(' \t2 : No ')
dec = check(input())
if dec == 2:
    exit(0)

Answer = random.Random(21)
print(' NOTE : YOU HAVE ONLY FIVE CHANCES TO GUESS THE NUMBER ')
print(' NOTE : ENTER VALUE FROM 1 TO 20 ')

guessCount = 0











'''



'''