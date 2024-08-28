def pastable(note, paper, x,y,r,c): # paste가 가능한지 확인 함수
    for i in range(r):    # 행렬을 돌며 값이 해당값에 1인지 확인 
        for j in range(c):
            if note[x+i][y+j] == 1 and paper[i][j] == 1: 
                return False  # 값이 있다면 False를 반환
            
    for i in range(r): # 붙일 수 있는 상태이니, note에 붙이기.
        for j in range(c):
                if paper[i][j] == 1:
                    note[x+i][y+j] = 1
    return True #

def rotate(paper, r,c):
    tmp = [[0] * 12 for _ in range(12)]

    for i in range(r):
        for j in range(c):
            tmp[i][j] = paper[i][j]

    for i in range(c):
        for j in range(r):
            paper[i][j] = tmp[r-1-j][i]

    return paper ,c, r

    

# 입력값
n,m,k = map(int,input().split())
note = [[0] * 10 for _ in range(10)]

for _ in range(k):
    r,c = map(int,input().split())
    paper = [[0] * 12 for _ in range(12)]

    for i in range(r):   # 0으로 초기화 된 paper에 값 넣기
        row = list(map(int,input().split())) 
        for j in range(c):
            paper[i][j] = row[j]

    for rot in range(4):           # paper 회전 횟수
        is_paste = False        # paste를 붙였다면 break 해주는 변수 
        for x in range(n-r+1):     # 행 움직이면서 공간찾기
            if is_paste:
                break
            for y in range(m-c+1): # 열 
                if pastable(note, paper,x,y,r,c):
                    is_paste = True
                    break
    
        if is_paste:
            break
        print("#################")
        print(paper)
        print(note)
        paper,r,c = rotate(paper, r,c )
        
    
cnt =  sum(note[i][j] for i in range(n) for j in range(m))
print(cnt)