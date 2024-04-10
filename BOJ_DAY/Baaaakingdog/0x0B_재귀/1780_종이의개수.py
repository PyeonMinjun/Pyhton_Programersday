# 종이의 패턴 확인 및 갯수 세기
def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[x][y] != paper[i][j]:
                return False
    return True
    
# 종이 분할 및 재귀적으로 패턴 확인
def solve(x, y, z):
    if check(x, y, z):
        cnt[paper[x][y]+1] += 1
        return 
    
    n = z // 3
    for i in range(3):
        for j in range(3):
            solve(x + (i * n), y + (j * n), n)

# 메인 함수
if __name__ == "__main__":
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    cnt = [0, 0, 0]  # -1, 0, 1로 채워진 종이 갯수
    solve(0, 0, N)
    for i in range(3):
        print(cnt[i])
