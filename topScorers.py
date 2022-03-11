class userMainCode(object):
    @classmethod
    def marathon(cls,inp1,inp2,inp3):
        s = 0
        inp3.sort()
        for j in range(1,inp2+1):
            s += inp3[-j]
        return s

i1 = int(input())  # 4
i2 = int(input())  # 2
i3 = []

for i in range(i1):
    i3.append(int(input()))

obj = userMainCode()
print(obj.marathon(i1,i2,i3))
