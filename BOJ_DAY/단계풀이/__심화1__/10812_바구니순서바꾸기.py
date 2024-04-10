n,m = map(int,input().split())
arr = [0] * (n)

for i in range(1, n+1): # 1 ~ 10
    arr[i-1] = i
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for _ in range(m):
    i,j,k= map(int,input().split())
    
    arr = arr[:i-1]+ arr[k-1:j] + arr[i-1:k-1] + arr[j:]

print(" ".join(map(str,arr)))