def romans(inp):
    def getList(n):
        temp = []
        n = list(str(n)[::-1])  # 9 7 1
        print(n)
        for i in range(len(n) - 1, -1, -1): temp.append(int(n[i]) * 10 ** i)
        while 0 in temp: temp.remove(0)
        return temp

    dic = {0: '', 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X", 50: "L",
           100: "C", 500: "D", 1000: "M"}

    key = list(dic.keys())
    result = []
    output = ''

    if inp in key:
        print(dic[inp])
        return




for i in range(1,100):
    romans(i)