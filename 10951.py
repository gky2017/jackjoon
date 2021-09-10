# 입력이 들어올때까지 반복

import sys

while True:
    
    try :
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except :    
        break