# 조합
# 치킨집 m개 조합.
# 1. 좌표가 나오게 될텐데 이거에 대한 처리
import sys
input = sys.stdin.readline


# 1-집 2-치킨집
n, m = map(int,input().split()) 
board =[list(map(int,input().split())) for _ in range(n)]

def dfs(depth, start):
    # base
    global result
    val = 0

    if depth == m:
        total_distance = 0
        # 좌표 계산
        for hr,hc in house:
            min_distance = float('inf')
            for idx in select:
                cr, cc = chicken[idx]
                distance = abs(hr-cr) + abs(hc-cc)
                min_distance = min(min_distance,distance)
            total_distance += min_distance
        result  = min(result, total_distance)
        return
    # 다음 치킨위치의 dfs
    for i in range(start, len(chicken)):
        # 배열에 담자.
        select.append(i)
        dfs(depth+1, i+1)
        select.pop()

chicken = []
house = []
select = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken.append((i,j))

        elif board[i][j] == 1:
            house.append((i,j))


result = float('inf')

dfs(0,0)
print(result)