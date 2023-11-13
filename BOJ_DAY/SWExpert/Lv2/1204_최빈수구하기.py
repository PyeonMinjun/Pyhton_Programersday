t = int(input())

for tc in range(1,t+1):
    num = int(input())
    ns = list(map(int,input().split()))
    arr = [0] * 101
    
    for i in ns:
        arr[i] += 1
    
    if arr.count(max(arr)) > 1:
        arr = arr[::-1]
        print("#{} {}" .format(tc,100 - arr.index(max(arr))))
    else:
        print("#{} {}" .format(tc,arr.index(max(arr))))
        
    
