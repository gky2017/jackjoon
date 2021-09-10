# 더하기 사이클
import sys

n = int(sys.stdin.readline())
num = n
count = 0
while True:
    ten = num//10
    one = num%10
    res = (ten + one) % 10
    num = (one * 10) + res

    count += 1
    if (num == n):
        break
print(count)
