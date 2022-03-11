# Students start from one end and hop to the other end. One can step on a stone and add the
# number on the stone to their cumulative score or jump over a stone and land on the next stone. In
# this case, they get twice the points marked on the stone they land but do not get the points
# marked on the stone they jumped over.
# At most once in the journey, the student is allowed (if they choose) to do a ―double jump‖ – that
# is, they jump over two consecutive stones where they would get three times the points of the
# stone they land on but not the points of the stone they jump over
# The teacher expected his students to do some thinking and come up with a plan to get the
# maximum score possible. Given the numbers on the sequence of stones, write a program to
# determine the maximum score possible.

# Input:
# 6
# 1 2 3 4 5 6

# Output:
# 27
# ---------------------------------------------------------------------------------------------
def fun():
    n = int(input())
    lst = []
    for i in range(n): lst.append(int(input()))
    ind = []
    for i in range(2**len(lst)):
        temp = bin(i)[2:]
        if len(temp) == len(lst) and '000' not in temp: ind.append(temp[::-1])
    result = []
    for i in ind:
        s ,c = 0, 0
        for j in range(len(i)):
            if i[j] == '0': c += 1
            else:
                if c == 0: s += lst[j]
                elif c == 1:
                    s += 2*lst[j]
                    c = 0
                else:
                    s += 3*lst[j]
                    c = 0
        result.append(s)
    print(max(result))
fun()