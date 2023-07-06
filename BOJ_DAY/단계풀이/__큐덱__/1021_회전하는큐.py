from collections import deque

n,m = map(int, input().split())
# ns = []

k = list(map(int, input().split())) # [ 2,9,5]
q = deque(range(1,n+1))
print(q)
cnt = 0

for i in k:
    while q:
        if i == q[0]:
            q.popleft()
            break
        else:
            if q.index(i) <= len(q)//2:
                while i != q[0]:
                    q.append(q.popleft())
                    cnt += 1
            else:
                while i != q[0]:
                    q.appendleft(q.pop())
                    cnt += 1
                    
print(cnt)    



