n = int(input())
cnt = 0

for _ in range(n):
    ns = list(input())
    
    stk = []
    for i in ns:
        if i == "A":
            if stk:
                if stk[-1] == "A":
                    stk.pop()
                else:
                    stk.append("A")
            else:
                stk.append("A")
                
        elif i == "B":
            if stk:
                if stk[-1] == "B":
                    stk.pop()
                else:
                    stk.append("B")
            else:
                stk.append("B") 
    
    if not stk:
        cnt += 1

print(cnt)
         
                
                
    