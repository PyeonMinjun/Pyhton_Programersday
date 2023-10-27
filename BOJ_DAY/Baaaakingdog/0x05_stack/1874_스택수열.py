
n = int(input())

stk = []
cnt = 1
res = []

for _ in range(n):
    ns = int(input())
    
    while cnt <= ns:
        stk.append(cnt)
        res.append("+")
        cnt += 1
        
        
    if stk[-1] == ns:
        stk.pop()
        res.append("-")
    
    else:
        print("NO")
        exit(0)
print("\n".join(res))
    