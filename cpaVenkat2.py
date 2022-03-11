class pd:
    def __init__(self,uid,dc):
        self.uid = uid
        self.dc = dc

def main():
    t = int(input())
    lst = []
    for i in range(t):
        dic1 = {}
        uid = int(input())
        n = int(input())
        for j in range(n):
            temp = input()
            dic1[temp] = int(input())
        lst.append(pd(uid,dic1))
    t = int(input())
    dic2 = {}
    for i in range(t):
        temp = input()
        dic2[temp] = int(input())
    findDealer(lst,dic2)

def findDealer(inp1,inp2):
    userid = []
    com = []
    for dealer in inp1:
        tr = 0
        print(list(dealer.dc.keys()) == list(inp2.keys()))
        if list(dealer.dc.keys()) == list(inp2.keys()):
            for i in range(len(list(dealer.dc.keys()))):
                tr += list(inp2.values())[i]*(list(dealer.dc.values())[i]/100)
            userid.append(dealer.uid)
            com.append(tr)
    if userid: print(f'{userid[com.index(min(com))]}:{int(min(com))}')
    else: print('No Dealers Found')

if __name__ == "__main__":
    main()