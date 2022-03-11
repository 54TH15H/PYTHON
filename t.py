def adjFounder(arr,row,col):  # row 1, col 2
    status = {'t':0,'l':0,'d':0,'r':0,'tl':0,'tr':0,'dl':0,'dr':0}
    if row>0:
        if arr[row-1][col] == 1:
            status['t'] = 1
        if col > 0:
            if arr[row-1][col - 1] == 1:
                status['tl'] = 1
        if col < len(arr[row]) - 1:
            if arr[row-1][col + 1] == 1:
                status['tr'] = 1
    if row<len(arr)-1:
        if arr[row+1][col] == 1:
            status['d'] = 1
        if col > 0:
            if arr[row+1][col - 1] == 1:
                status['dl'] = 1
        if col < len(arr[row]) - 1:
            if arr[row + 1][col + 1] == 1:
                status['dr'] = 1
    if col>0:
        if arr[row][col-1] == 1:
            status['l'] = 1
    if col<len(arr[row])-1:
        if arr[row][col+1] == 1:
            status['r'] = 1

    return dicToList(status)