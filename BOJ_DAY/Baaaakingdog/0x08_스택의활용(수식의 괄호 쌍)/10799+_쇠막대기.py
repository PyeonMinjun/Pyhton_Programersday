n = list(input())
stk = []
res = 0
for i in range(len(n)):
    if n[i] == "(":
        stk.append("(")
        
    elif n[i] == ")":
        if n[i-1] == "(":
            stk.pop()
            res += (len(stk))
        else:
            stk.pop()
            res += 1
print(res)
