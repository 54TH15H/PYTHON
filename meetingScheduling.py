
# MEETING SCHEDULING.

# TAKES YWO PARAMETERS AS INPUT AND COMPARES THE TIMES(INPUTS).
def timeComparing(t1, t2):
    t1h,t1m = t1.split(':')
    t2h,t2m = t2.split(':')

    if int(t1h)<int(t2h):
        return 1
    elif int(t1h)>int(t2h):
        return -1
    else:
        return 0

# CALCULATES THE TIME DIFFERENCE AND GIVES THE OUTPUT IN MINUTES.
def timeDiff(t1, t2):
    t1h, t1m = t1.split(':')
    t2h, t2m = t2.split(':')

    dh = int(t1h) - int(t2h)
    dm = int(t1m) - int(t2m)

    return dh*60 + dm

# CALCULATES FREE TIME TO SCHEDULE THE MEETING.
def findFreeTime(p):

    f = []
    i = 0
    for i in range(0,len(p)):
        if i == 0:
            if timeDiff(p[i][0],startTime) >= meetingDuration:
                f.append([startTime,p[i][0]])
        else:
            if timeDiff(p[i][0],p[i-1][1]) >= meetingDuration:
                f.append([p[i-1][1],p[i][0]])

    if timeDiff(endTime,p[i][1]) >= meetingDuration:
        f.append([p[i][1],endTime])

    return f

def timeInHr(time):
    t,m = time.split(':')
    return t

def  unwantedTimeRem():
    for i in p1meet:
        for j in p2meet:
            st1 = timeInHr(i[0])
            et1 = timeInHr(i[1])
            st2 = timeInHr(j[0])
            et2 = timeInHr(j[1])




startTime = '09:00'
endTime = '16:00'
meetingDuration = 30

# MEETING TIMINGS.
p1meet = [['10:00','11:31'],['12:00','13:00'],['14:00','15:00']]
p2meet = [['10:30','11:00'],['11:30','12:30'],['14:00','15:31']]

# FREE TIME WITHOUT ANY MEETINGS.
# [['09:00','10:00'],['13:00','14:00'],['15:00','16:00']]
# [['09:00','10:30'],['11:00','11:30'],['12:30','14:00']]

m1 = findFreeTime(p1meet)
m2 = findFreeTime(p2meet)

print(m1)
print(m2)




'''

output = [['09:00','09:30'],['09:30','10:00'],['13:00','13:30'],['13:30','14:00']]


'''