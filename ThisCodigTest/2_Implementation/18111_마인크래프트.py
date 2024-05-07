import sys

input = sys.stdin.readline
n,m,b = map(int,input().split())
board =  [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
def check(board,lv,b):
    sc = 0
    c = 0
  
    for i in range(n):
        for j in range(m):
            z = board[i][j] - lv
            if z > 0: # 블록 채움
                b += z
                sc += 2 * z
                
            else: # 블록 파기
                c += -z
    if b < c:
        return INF
    return sc + c
 
msc = INF
mlv = 0   

for lv in range(256, -1,-1):
    sc = check(board, lv, b)
    if msc > sc:
        msc = sc
        mlv = lv
print(msc, mlv)
    