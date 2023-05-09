n = int(input())
cnt = 2
arr =[2,3]

for i in range(1,16):
    arr.append(arr[i]+ cnt)
    cnt *= 2

res = arr[n]
print(res * res)