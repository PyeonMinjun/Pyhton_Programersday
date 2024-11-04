import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

dx = [0, 1, 1]  # 방향: 오른쪽, 대각선, 아래쪽
dy = [1, 1, 0]

# 범위 밖을 벗어났는지 체크하는 함수
def oob(x, y):
    return x < 0 or x >= n or y < 0 or y >= n

def sim(x, y, before_dir):
    global ans
    if x == n - 1 and y == n - 1:
        ans += 1
        return

    for dir in range(3):
        # 45도 제한 조건
        if (before_dir == 0 and dir == 2) or (before_dir == 2 and dir == 0):
            continue
        
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if oob(nx, ny) or board[nx][ny]:
            continue
        
        # 대각선으로 이동할 때에 한해 추가 체크
        if dir == 1 and (board[nx][y] or board[x][ny]):
            continue
        
        sim(nx, ny, dir)

sim(0, 1, 0)
print(ans)
