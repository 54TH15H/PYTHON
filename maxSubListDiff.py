def fun():

    def nValue(inp):
        if inp >= 4 and inp <= 10 ** 5:
            return inp
        else:
            print(' Invalid entry,try again ')
            return nValue(int(input()))

    def checkElement(inp):
        if int(inp) >= 1 and int(inp) <= 10 ** 4:
            return int(inp)
        else:
            print(' Invalid entry,try again ')
            return checkElement(input())

    def abs_min_max(size, values):
        from itertools import islice
        # list_len = len(values)
        length_to_split = [1, 1, 1, size - 3]
        Input = iter(values)
        output = [list(islice(Input, elem))
                  for elem in length_to_split]

        res = 0
        result = []
        for i in output:
            for j in range(len(i)):
                res = res + i[j]
            result.append(res)
            res = 0

        # try:
        #
        #     for i in output[0][i]:
        #         P = P + i
        #         print(P)
        #     for j in output[1][j]:
        #         Q = Q + j
        #         print(Q)
        #     for i in output[2][i]:
        #         R = R + i
        #     for j in output[3][j]:
        #         S = S + j
        # except UnboundLocalError:m
        #     pass

        print(max(result) - min(result))

    a = nValue(int(input()))                    # 4
    arr_val = []                                # 1,2,3,4
    for i in range(a):
        arr_val.append(checkElement(input()))

    abs_min_max(a, arr_val)

fun()