n = int(input())


for cnt in range(n):
    cnt += 1
    a = int(input())
    ns = list(map(int,input().split()))

    maxo = -1
    val = -1
    arr = [0] * 1000

    for i in ns:
        arr[i] += 1
        
        if arr[i] > maxo:
            maxo = arr[i]
            val = i
        elif arr[i] == maxo:
            if val < i:
                val = i 

    print("#{} {}" .format(cnt, val))
    
