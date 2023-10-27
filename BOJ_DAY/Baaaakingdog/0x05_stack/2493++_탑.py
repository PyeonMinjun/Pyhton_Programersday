n = int(input())
top = list(map(int,input().split()))

stk = [(5000001,0)]
res = []

for i in range(n):
    h = top[i]
    while stk[-1][0] < h:
        stk.pop()
    res.append(stk[-1][1])
    stk.append((h,i+1))
    
print(res)  
        