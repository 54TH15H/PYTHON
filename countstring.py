
# IT COUNTS THE INDIVIDUAL LETTERS REPETITION IN YOUR STRING

def count(s):
    z = []
    k = 0
    a = list(s)
    b = set(s)
    b = list(b)
    for i in b:
        k += 1
    for i in range(k):
        z.append(0)
    for i in range(0, k):
        for j in a:
            if b[i] == j:
                z[i] += 1
            else:
                continue
                
    for i in range(0, k):
        print('{} : {}'.format(b[i], z[i]))


x = input('Enter a word : ')
count(x)
