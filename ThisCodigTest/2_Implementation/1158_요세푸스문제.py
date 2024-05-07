import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
arr = deque([i+1 for i in range(n)])
res = []



while arr:
    for _ in range(k-1):
        arr.append(arr.popleft())
    res.append(arr.popleft())
    

print("<{}>" .format(str(res)[1:-1]))