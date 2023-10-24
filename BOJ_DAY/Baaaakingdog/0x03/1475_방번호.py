n = list(input())
arr = [0] * 10
cnt = 0

for i in n:
    if int(i) == 6 or int(i) == 9:
        cnt += 1
        continue
    
    arr[int(i)] += 1

a = max(arr)

if cnt % 2 == 1:
    cnt += 1

if a > (cnt//2):
    print(a)
else:
    print(cnt//2)