# 최솟값, 최댓값 출력

import sys
n = int(sys.stdin.readline())
num_n = list(map(int, sys.stdin.readline().split()))

print('{} {}'.format(min(num_n), max(num_n)))