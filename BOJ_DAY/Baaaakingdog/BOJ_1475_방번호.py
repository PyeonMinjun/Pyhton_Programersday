n = int(input())
arr = [0] * 10

n = list(str(n))

for i in n:
    i = int(i)
    if i == 6 or i ==9:
        if arr[6] < arr[9]:
            arr[6] += 1
        else:
            arr[9] += 1
    else:        
        arr[i] += 1

print(max(arr))

