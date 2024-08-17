from itertools import combinations


n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]


chiken = []
house = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chiken.append((i,j))
        elif board[i][j] == 1:
            house.append((i,j))

res = float("inf")

for chi in combinations(chiken, m): # (1,2) (1,3)...
    total_distance = 0

    for hx,hy in house:
        min_distance = float('inf')
        for cx, cy in chi:
            distance = abs(hx-cx) + abs(hy- cy)
            min_distance = min(distance,min_distance)
        
        total_distance += min_distance
    res = min(res,total_distance)

print(res)