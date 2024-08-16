def dfs(dep, start, tas, over):
    global res
   # dep 밑에 인자값이랑 비교하면서 같으면 return
    if over > overcalorie:
        return
    
    res = max(tas, res)

    for j in range(start, cnt):
     dfs(dep + 1, j + 1, tas + board[j][0], over + board[j][1])

t = int(input())
for tc in range(t):
    cnt, overcalorie = list(map(int, input().split()))
    res = 0
    board = [list(map(int, input().split())) for _ in range(cnt)]
    # for문
    dfs(0, 0, 0, 0 )# 인자값 하나 추가하고  # 초기 호출
    print("#{} {}" .format(tc+1,res))
