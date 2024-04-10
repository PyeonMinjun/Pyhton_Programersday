import sys
input = sys.stdin.readline
n = int(input())

dat = []

for _ in range(n):
    m = int(input())
    if m == 0:
        dat.pop()
    else:
        dat.append(m)

print(sum(dat))