n,cost = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]    




max_gold = 0

for row in range(n):
    for col in range(n):
        for k in range(2 * (n-1) + 1):
            cnt = 0
            for i in range(n):
                for j in range(n):
                    if abs(row -i) + abs(col -j) <= k:
                        cnt += board[i][j]
            # 춧 = cnt

            if cnt * cost >= k * k + (k+1) * (k+1):
                max_gold = max(max_gold, cnt)

print(max_gold)