class UserMainCode:
    @classmethod
    def find(cls, input1, input2, input3): # 1 4 5
        count = 0
        lst = []
        if input1 == 1:
            count += 2
        else:
            for i in [input2,input3]:
                for j in [input2,input3]:
                    lst.append([i,j])
            count += 5

        return count

i1 = int(input())
i2 = int(input())
i3 = int(input())
obj = UserMainCode()
print(obj.find(i1,i2,i3))