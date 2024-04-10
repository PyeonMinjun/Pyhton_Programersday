import sys
from collections import deque
input = sys.stdin.readline

n = deque([i+ 1 for i in range(int(input()))])

while len(n) != 1:
    n.popleft()
    x = n.popleft()
    n.append(x)

print(n[0])