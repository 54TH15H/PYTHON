
# CONTACT SEARCHING USING KEYPAD

dic = { 0:[''] ,1:[''] ,2:['a','b','c'] , 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}

# ACCEPTS ANY TYPE VALUES BUT RETURNS THE SAME VALUE IF THE INPUT IS AN INTEGER.
def check(n):
    try:
        return int(n)
    except ValueError:
        print(' ENTER ONLY INTEGER VALUES : ',end = '')
        return check(input())

# ACCEPTS AN INTEGER AND MAKES A LIST OF INDIVIDUAL DIGITS IN THE INPUT.
def intToList(t):
    r = 0
    l = []
    while t>0:
        r = t%10
        t = t//10
        l.append(r)
    return revList(l)

def searchContact():
    n = input(' ENTER A NAME TO SEARCH : ')
    n = n.lower()
    if n in lst:
        print("THE NAME {} IS AVAILABLE AT POSITION {}".format(n,lst.index(n)+1))
    else:
        print(' THE NAME {} IS NOT AVAILABLE '.format(n))



#  REVERSING THE LIST.
def revList(a):
    b = [0,0,0,0,0,0,0,0,0,0]
    for i in range(-1,-(len(a)+1),-1):
        b.remove(0)
        b.insert(abs(i+1),a[i])
    return b

# GETTING LIST OF NAMES BASED ON NUMBERS.
def fun(li):

    print()
    for j0 in dic.get(li[0]):
        for j1 in dic.get(li[1]):
            for j2 in dic.get(li[2]):
                for j3 in dic.get(li[3]):
                    for j4 in dic.get(li[4]):
                        for j5 in dic.get(li[5]):
                            for j6 in dic.get(li[6]):
                                for j7 in dic.get(li[7]):
                                    for j8 in dic.get(li[8]):
                                        for j9 in dic.get(li[9]):
                                            lst.append(j0+j1+j2+j3+j4+j5+j6+j7+j8+j9)

    print(lst)

lst = []
inp = check(input(' ENTER A NUMBER : '))
print(" \n WE GET CONTACT NAMES STARTING WITH BELOW RESULTS, IF WE ENTER {} IN THE CONTACTS APPLICATION. ".format(inp))
fun(intToList(inp))
searchContact()
