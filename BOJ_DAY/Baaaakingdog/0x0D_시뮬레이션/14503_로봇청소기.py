N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

vis  = [[False] * N for _ in range(M)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


ans = 0

while True:
    if board[x][y] == 0:
        ans += 1
    board[x][y] = -1
   # 현재 칸의 주변 4칸중 청소되지 않는 빈칸이 있는 경우,
    clean = False
    for i in range(4):
        d = (d +3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if board[nx][ny] == 0:
            x,y = nx,ny
            clean = True
            break

    if clean:
        continue
        
    if board[x - dx[d]][y - dy[d]] == 1:
        break

    x = x - dx[d]
    y = y - dy[d]

print(ans)





# ans = 0

# while True:
#     # 현재 위치가 청소되지 않은 빈 칸일 경우 청소
#     if board[x][y] == 0:
#         ans += 1
#     board[x][y] = -1  # 청소된 칸으로 표시

#     cleaned = False  # 네 방향 중 청소가 된 곳이 있는지 확인
#     for _ in range(4):
#         d = (d + 3) % 4  # 왼쪽으로 회전
#         nx, ny = x + dx[d], y + dy[d]
#         if board[nx][ny] == 0:  # 청소하지 않은 빈 칸이 있으면 이동
#             x, y = nx, ny
#             cleaned = True
#             break
        
#     if cleaned:
#         continue

#     # 네 방향 모두 청소가 되어 있거나 벽인 경우
#     # 뒤가 벽으로 막혀 있으면 종료
#     if board[x - dx[d]][y - dy[d]] == 1:
#         break

#     # 벽이 아니라면 후진
#     x -= dx[d]
#     y -= dy[d]

# print(ans)
