# 10871
# X보다 작은 수

import sys
n, x = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if A[i] < x:
        print(A[i], end = '')