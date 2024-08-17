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

res = float('inf')
for chi in combinations(chiken, m):


    total_distance = 0
    for hx,hy in house:
        
        distance = float('inf')
        for cx,cy in chi:
            
            distance = min(abs(hx - cx) + abs(hy - cy), distance)
        
        total_distance += distance
    
    res = min(total_distance, res)

print(res)
