# [1,2,3,4,5]
# 2개 수열


ns = [1,3,5,7,9]
n = 5
m = 2


arr = [0] * 10
isused = [False] * 10

def func(k,start):
    # basecondision
    if k == 3:
        for i in range(3):
            print(arr[i], end = " ")
        print()
        return
    
  
    for i in range(start,5+1): # 처음부터 끝까지 범위
            arr[k] = i     # 해당 값에 값을 넣고, 
            func(i, k+1)

func(0,0)


