import sys
from itertools import product
def countDivisibleSubseq(N,Arr):
    slices=[]
    for doslice in product([True,False], repeat=len(Arr)-1):
        start=0
        for i, slicehere in enumerate (doslice,1):
            if slicehere:
                slices.append(Arr[start:i])
                start=i
        slices.append(Arr[start:])
    count=len(set(Arr))
    for i in range(len(slices)):
        if len(slices[i])>=1:
            for j in range(len(slices[i])-1,0,-1): #2,0,-1
                    if slices[i][j] % slices[i][j-1]==0:
                        count+=1
    return count
def main():
    N=int(sys.stdin.readline().strip())
    Arr=[]
    for _ in range(N):
        Arr.append(int(sys.stdin.readline().strip()))
    result=countDivisibleSubseq(N,Arr)
    print(result)
if __name__ == "__main__":
    main()