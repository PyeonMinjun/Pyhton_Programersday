from collections import deque
t = int(input())

for _ in range(t):
    n,m = (map(int,input().split()))
    ns = list(map(int,input().split()))
    q = deque()
    
    for i,x in enumerate(ns):
        q.append((i,x))
        
    ns.sort()
    cnt = 0
    while q:
        i,x = q.popleft()
        if x == ns[-1]:
            ns.pop()
            cnt += 1
            if i == m:
                print(cnt)
                break
        else:
            q.append((i,x))
        

