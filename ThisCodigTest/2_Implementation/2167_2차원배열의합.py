import sys
input = sys.stdin.readline
n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

k = int(input())

for _ in range(k):
    i,j,x,y = (map(int,input().split()))
    res = 0

    for r in range(i, x+1):
        for c in range(j, y+1):
            res += board[r-1][c-1]
    
    print(res)