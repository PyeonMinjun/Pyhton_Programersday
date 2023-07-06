from collections import deque


# 1 2 3 4 5 6 7
# 3 4 5 6 7 1 2  # 3을뺌

# 4 5 6 7 1 2
# 6 7 1 2 4 5  # 6을 뺌

# 7 1 2 4 5
# 2 4 5 7 1  # 2를 뺌


n, k = map(int, input().split())
arr =  deque(range(1,n+1)) # deque()
# arr = [i+1 for i in range(n)]

res = []


while arr:
    for _ in range(k-1):
        arr.append(arr.popleft())
    res.append(arr.popleft())
        
