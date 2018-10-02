import time
import random

#반복적 피보나치 수열

def iterfibo(n):
    if n <= 1:
        return n
    fiboF = 1
    fiboL = 1
    for i in range(n - 1):
        fiboF,fiboL = (fiboL,fiboF+fiboL)
    return fiboF

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


while True:
    nbr = int(input('Enter a number:'))
    if nbr == -1:
        break

    # 반복 피보나치
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print('iterFibo(%d) = %d, time %.6f' % (nbr, fibonumber, ts))

    # 재귀 피보나치

    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print('Fibo(%d) = %d, time %.6f' % (nbr, fibonumber, ts))
