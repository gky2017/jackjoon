import sys

n, x = map(int,sys.stdin.readline().split())

N = list(map(int, sys.stdin.readline().split()))


for i in range(n):
    if x > N[i]:
        print(N[i], end=' ')