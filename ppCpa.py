class BQH:
    def __init__(self,uid,name,capacity,plist,alist):
        self.uid = uid
        self.name = name
        self.capacity = capacity
        self.plist = plist
        self.alist = alist

class HMS:
    def __init__(self,blist): self.blist = blist

    def bill(self,g,amlist):
        for hall in self.blist:
            if g <= hall.capacity:
                for j in amlist:
                    if j in hall.alist: continue
                    else: break
                else:
                    for j in hall.plist:
                        if g>=j[1] and g<=j[2]:
                            bill = j[0]*g
                            bill = bill + (bill*13)/100
                            return bill
                    else: return "Hall Not Found"
        else: return "Hall Not Found"

def main():
    t = int(input())
    BQHList = []
    for i in range(t):
        uid = int(input())
        name = input()
        capacity = int(input())
        pl = int(input())
        plist = []
        for j in range(pl):
            temp = []
            for k in range(3):
                temp.append(int(input()))
            plist.append(tuple(temp))
        al = int(input())
        alist = []
        for j in range(al):
            alist.append(input().lower())
        BQHList.append(BQH(uid,name,capacity,plist,alist))

    t = int(input())
    j = int(input())
    lst = []
    for i in range(j): lst.append(input().lower())

    hms = HMS(BQHList)
    print(hms.bill(t,lst))

if __name__ == "__main__":
    main()
