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
        # 좌표 계산
        for hr,hc in house:
            dist = 2 * n
            for cr, cc in select:
                tmp = abs(hr-cr) + abs(hc-cc)
                if tmp <  dist:
                    dist = tmp
            val += dist

        if val < result:
            result = min(val,result)
            return

    
    # 다음 치킨위치의 dfs
    for i in range(start, len(chicken)):
        # 배열에 담자.
        select.append(chicken[i])
        dfs(depth+1, start+1)
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


result = n * 2 * len(house)

dfs(0,0)
print(result)