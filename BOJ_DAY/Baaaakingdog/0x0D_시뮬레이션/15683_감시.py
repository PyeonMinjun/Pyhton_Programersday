#(x,y)에서 dir방향으로 진행을 하며 벽을 만날때마다 모든 빈칸을 7로 바꿈.
def upd(x,y,direction):
    global board2
    # dx dy , dir
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    dir = direction % 4
    # 반복문을 통해 배열값 넘어값이나 6이라면 return
    while True:
        x += dx[dir]
        y += dy[dir]
        if x < 0 or x >= n or y < 0 or y >= m or board2[x][y] == 6:
            return
    # CCTV일때 처리
        if board2[x][y] != 0:
            continue
    # 나머지 값에 대해 7처리
        board2[x][y] = 7

n,m = map(int,input().split())
board1 = [] # 원본
board2 = [] # 원본 복사
mn = 0 # 0의 개수 
cctv = [] ## cctv 

for i in range(n):
    row = list(map(int,input().split()))
    board1.append(row)

    for j in range(m): 
        if row[j] != 0 and row[j] != 6:
            cctv.append((i,j))
        if row[j] == 0:
            mn += 1

#pow 함수를 이용해서 총 조합수 계산
coll = pow(4,len(cctv))

for tmp in range(coll): # 모든 조합의 경우의 수에서
    board2 = [row[:] for row in board1] # 원본에서 복사.
    for i in range(len(cctv)): # cctv 수만큼
        dir = tmp % 4 # 해당 dir을 구하고
        tmp //= 4
        x, y = cctv[i]
        if board1[x][y] == 1:
            upd(x,y,dir)
        if board1[x][y] == 2:
            upd(x,y,dir)
            upd(x,y,dir+2)
        elif board1[x][y] == 3:
            upd(x, y, dir)
            upd(x, y, dir + 1)
        elif board1[x][y] == 4:
            upd(x, y, dir)
            upd(x, y, dir + 1)
            upd(x, y, dir + 2)
        elif board1[x][y] == 5:
            upd(x, y, dir)
            upd(x, y, dir + 1)
            upd(x, y, dir + 2)
            upd(x, y, dir + 3)

    val = sum(1 for i in range(n) for j in range(m) if board2[i][j] == 0)
    mn = min(mn, val)

print(mn)
