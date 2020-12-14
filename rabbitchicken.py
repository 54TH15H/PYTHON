
def solve(heads, legs):
    error_msg = "No solution"
    chicken_count = 0
    rabbit_count = 0
    temp_chicken_count = 0
    if legs % 2 == 0 and legs >= heads*2 and legs <= heads*4:
        while (rabbit_count * 4 + chicken_count * 2) != legs:

            rabbit_count = legs // 4
            chicken_count = heads - rabbit_count
            if (rabbit_count * 4 + chicken_count * 2) == legs:
                print(chicken_count+temp_chicken_count, rabbit_count)
                break
            else:
                legs -= 4
                temp_chicken_count += 2
                heads -= 2
                continue

    else:
        print(error_msg)
   
solve(1, 4)
