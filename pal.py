def countPalindrome(input1,input2):
    lst = input1.split(' ')
    count = 0
    print(lst)
    for i in lst:
        if i == i[::-1]:
            count += 1

    print(count)


input1 = 'this isi level 71'
input2 = 16
countPalindrome(input1,input2)