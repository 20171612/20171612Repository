import time
import random


def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1


def recbinsearch(L, l, u, target):
    if l > u:            #타겟이 리스트최대 최소값 밖에있을경우에도 l>u에서 처리됨
        return -1
    else: 
        m = (l + u)//2
        
        if target == L[m]:
            return L[m]
        elif target < L[m]:
            return recbinsearch(L,l,m-1,target)
        else:
            return recbinsearch(L,m+1,u,target)   #에러상황설명 ex) [1,2,3,4,5]리스트가 있을때 u값에는 len(numbers)즉 요소의 개수가 들어가서 5가 들어감 하지만 리스트안 5의 인덱스는 4이기때문에 L[5]가 들어갈경우 인덱스범위를 벗어나 에러가발생


numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)
numbers[0] = 0               
numbers[-1] = 999999         # solve1)numbers의 최대값과 최소값을 지정하여 target이 u안쪽에 위치하도록 조정
numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]


ts = time.time()

# binary search - recursive
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers)-1, target)   # solve2)마지막 인덱스의 숫자와 요소의개수의 수가 일치하도록 len(numbers)에 -1해줌
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))
