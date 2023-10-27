n = int(input())
tops = list(map(int,input().split()))

res = []
stk = []
stk.append((100000001,0))

for i in range(n):
    h = tops[i]
    while stk[-1][0] < h:
        stk.pop()
    res.append(stk[-1][1])
    stk.append((h,i+1))
    


print(" ".join(map(str,res)))