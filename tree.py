import math
def tree(inp):
    inp = list(str(inp))
    result = []
    if inp[0] == '0':
        print(1)
        return
    else:
        result.append(inp[0])
        inp.remove('1')
        for i in result:
            if i == '1':
                if len(inp) != 0:
                    result.append(inp[0])
                    inp.remove(inp[0])
                else:
                    break

                if len(inp) != 0:
                    result.append(inp[0])
                    inp.remove(inp[0])
                else:
                    break
            elif i == '0':
                result.append('-')
                result.append('-')
            else: continue

    # print(len(result))
    length = 0
    for j in result:
        if j == '1' or j == '0':
            length += 1

    # print(length)
    print(math.ceil(math.log2(length+1)))

inp = 0
tree(inp)

# inp 1
# res = 1 0 0 - - - -
# 1 0 0 1
#
# 1 0 0 - - - - 1
# 0 1 2 3
