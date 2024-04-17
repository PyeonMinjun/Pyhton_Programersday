from operator import itemgetter
def solution(foodtimes, k):
    result = 0
    arr = [] # 빈 배열선언 
    n = len(foodtimes) # foodtimes 길이, 총개수
    for i in range(n): # 모든 배열의 길이를 돌며,
        arr.append((foodtimes[i],i+1)) #  foodtimes , 음식의 순번 으로 튜플을 배열에 저장함.
    
    arr.sort() # foodtimes를 기준으로 정렬
    
    preval = 0 
    for i, letter in enumerate(arr): # i가 필요한 이유는 k보다 큰 값이 할당 되었을때 해당 기준으로 자르기 위함. \
                                        # 따라서, enumerate로 arr 설정. ex. (0,(3,1)) 
        diff = letter[0] - preval # 현재 높이 값
        if diff != 0:  # 높이가 다르다면 진행 같디면, 더 앞에서 제거했기때문에 또 연산할 필요가 없음.
            spend = diff * n  # 빼야할 값
            if k >= spend: # 남은값이 더 크다면 정상적으로 진행
                k -= spend # 값 빼줌
                preval = letter[0] # 전의 값을 높이 값을 저장해두고 diff를 바꿔줌.
            else: # 남은 값인 k보다 빼야할 spend의 값이 크다면 ?
                k %= n # 나머지를 통해 순번위치를 지정 
                leftarr = sorted(arr[i:], key = itemgetter(1)) # 남은 배열 / 위에서 정의한 순번을 가지고 재정렬
                return leftarr[k][1] # (5,2)(6,4)(5,5) 순으로 정렬된 값을 첫번째배열의 4를 출력.
        n -= 1 # 밑값을 하나씩 줄여감.
    
    return -1 # 만약 배열을 다돌았는데 값이 없다면 총 foodtime보다 k값이 큰것 -1을 출력


print(solution([3,1,2],5))