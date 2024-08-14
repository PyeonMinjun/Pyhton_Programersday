
def upd(x, y, direction, board2):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir = direction % 4
    while True:
        x += dx[dir]
        y += dy[dir]
        if x < 0 or x >= n or y < 0 or y >= m or board2[x][y] == 6:
            return
        if board2[x][y] != 0:
            continue
        board2[x][y] = 7

n, m = map(int, input().split())
board1 = []
cctv = []
mn = 0

for i in range(n):
    row = list(map(int, input().split()))
    board1.append(row)
    for j in range(m):
        if row[j] != 0 and row[j] != 6:
            cctv.append((i, j))
        if row[j] == 0:
            mn += 1

# pow 함수를 사용하여 총 조합 수 계산
total_configurations = pow(4, len(cctv))

for tmp in range(total_configurations):
    board2 = [row[:] for row in board1]
    brute = tmp
    for i in range(len(cctv)):
        dir = brute % 4
        brute //= 4
        x, y = cctv[i]
        if board1[x][y] == 1:
            upd(x, y, dir, board2)
        elif board1[x][y] == 2:
            upd(x, y, dir, board2)
            upd(x, y, dir + 2, board2)
        elif board1[x][y] == 3:
            upd(x, y, dir, board2)
            upd(x, y, dir + 1, board2)
        elif board1[x][y] == 4:
            upd(x, y, dir, board2)
            upd(x, y, dir + 1, board2)
            upd(x, y, dir + 2, board2)
        elif board1[x][y] == 5:
            upd(x, y, dir, board2)
            upd(x, y, dir + 1, board2)
            upd(x, y, dir + 2, board2)
            upd(x, y, dir + 3, board2)

    val = sum(1 for i in range(n) for j in range(m) if board2[i][j] == 0)
    mn = min(mn, val)

print(mn)
