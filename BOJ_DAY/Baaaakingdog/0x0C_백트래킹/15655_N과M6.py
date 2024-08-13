import sys

# 최대 10개의 숫자를 선택하는 배열 초기화
arr = [0] * 10  # 선택된 숫자의 인덱스를 저장
isused = [False] * 10  # 숫자의 사용 여부를 저장
n, m = map(int, input().split())
board = list(map(int, input().split()))
board.sort()  # 숫자 정렬

def func(k):
    # m개의 숫자를 모두 선택한 경우
    if k == m:
        for i in range(m):
            print(board[arr[i]], end=' ')
        print()  # 한 조합을 출력한 후 줄바꿈
        return
    
    st = 0  # 시작 지점
    if k != 0:
        st = arr[k - 1] + 1  # k != 0인 경우, 이전 인덱스보다 큰 인덱스만 사용

    for i in range(st, n):
        if not isused[i]:  # 아직 i가 사용되지 않았으면
            arr[k] = i  # k번째 인덱스를 i로 정함
            isused[i] = True  # i를 사용되었다고 표시
            func(k + 1)  # 다음 인덱스를 정하러 한 단계 더 들어감
            isused[i] = False  # k번째 인덱스를 i로 정한 모든 경우에 대해 다 확인했으니 i를 이제 사용되지 않았다고 명시함

func(0)
