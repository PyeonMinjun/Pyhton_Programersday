n,m =  map(int,input().split())

arr = [0] * 10 # 수열을 담을 배열
isused = [0] * 10 # 특정 수가 쓰였는지를 true false로 나타내는 배열

def func(k): # 현재 k개까지 수를 택했음.
    if k == m: # m개를 모두 택했으면
        for i in range(m):
            print(arr[i], end=" ")  # arr에 기록해둔 수를 출력
        print()
        return
    
    # 백트래킹 
    for i in range(1,n+1): # 1부터 n까지의 수에 대해
        if not(isused[i]): # 아직 i가 사용되지 않았으면
            arr[k] = i # k번째 수를 i로 정함
            isused[i] = 1 # i를 사용되었다고 표시
            func(k+1) # 다음 수를 정하러 한 단계 더 들어감
            isused[i]= 0 # k번째 수를 i로 정한 모든 경우에 대해 다 확인했으니 i를 이제 사용되지않았다고 명시함. 

func(0)