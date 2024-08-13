# 입력값
n,m = map(int,input().split())

#반복문에서 n+1까지 도니까 [0] 추가
board = list(map(int,input().split())) + [0] 
# 정렬을 이행해서 뽑자.
board.sort()
# 배열 선언
# arr 데이터 저장할 배열
arr = [0] * 10
# 배열에 들어갔는지 확인하는 배열
isused = [False] * 10


# 함수 선언
def func(k):
# base condision
    if k == m:
        ## 반복문을 돌며 출력
        for i in range(m):
            print(arr[i], end = " ")
        print()
        return
    
    # backtracking
    for i in range(1, n+1):
        if not isused[i]: # 방문하지않았다면,
            arr[k] = board[i] # k번째에 숫자 넣고
            isused[i] = True # 방문했다 표시
            func(k+1) # 탐색하러 한단계 들어감
            isused[i] = False # 방문 해제

func(0)