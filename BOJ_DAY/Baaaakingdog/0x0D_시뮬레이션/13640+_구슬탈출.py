from collections import deque

# 방향 설정 (상, 우, 하, 좌)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 입력 처리
n, m = map(int, input().split())
board = []
red = blue = None

for i in range(n):
    row = list(input().strip())
    board.append(row)
    for j in range(m):
        if row[j] == 'R':
            red = (i, j)
            board[i][j] = '.'  # R 위치를 빈칸으로 변경
        elif row[j] == 'B':
            blue = (i, j)
            board[i][j] = '.'  # B 위치를 빈칸으로 변경

# 4차원 배열 생성 및 BFS 준비
dist = [[[[ -1 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
q = deque([(red[0], red[1], blue[0], blue[1])])
dist[red[0]][red[1]][blue[0]][blue[1]] = 0

# BFS 시작
while q:
    rx, ry, bx, by = q.popleft()
    cnt = dist[rx][ry][bx][by]

    # 10번 넘게 탈출 못하면 실패
    if cnt >= 10:
        print(-1)
        exit()

    for i in range(4):
        n_rx, n_ry, n_bx, n_by = rx, ry, bx, by

        # Blue 이동
        while board[n_bx + dx[i]][n_by + dy[i]] == '.':
            n_bx += dx[i]
            n_by += dy[i]
        # Blue가 구멍에 빠지면 실패
        if board[n_bx + dx[i]][n_by + dy[i]] == 'O':
            continue

        # Red 이동
        while board[n_rx + dx[i]][n_ry + dy[i]] == '.':
            n_rx += dx[i]
            n_ry += dy[i]
        # Red가 구멍에 빠지면 성공
        if board[n_rx + dx[i]][n_ry + dy[i]] == 'O':
            print(cnt + 1)
            exit()

        # Red와 Blue가 겹쳤을 때
        if n_rx == n_bx and n_ry == n_by:
            if i == 0:  # 위쪽
                if ry < by:
                    n_ry -= 1
                else:
                    n_by -= 1
            elif i == 1:  # 오른쪽
                if rx < bx:
                    n_rx -= 1
                else:
                    n_bx -= 1
            elif i == 2:  # 아래쪽
                if ry > by:
                    n_ry += 1
                else:
                    n_by += 1
            else:  # 왼쪽
                if rx > bx:
                    n_rx += 1
                else:
                    n_bx += 1

        # 방문한 적 있으면 continue
        if dist[n_rx][n_ry][n_bx][n_by] != -1:
            continue

        dist[n_rx][n_ry][n_bx][n_by] = cnt + 1
        q.append((n_rx, n_ry, n_bx, n_by))

# 10번 이내에 탈출 못하면 실패
print(-1)
