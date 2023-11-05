n = list(input())
stk = []
num = 1
res = 0

for i in range(len(n)):
    if n[i] == '(':
        stk.append('(')
        num *= 2
        
    elif n[i] == '[':
        stk.append('[')
        num *= 3
    
    elif n[i] == ')':
        if stk[-1] != '(':
            print(0)
            exit(0)
            
        
        elif n[i-1] == '(': 
            res += num
        stk.pop()
        num //= 2
            
            
    
    elif n[i] == "]":
        if stk[-1] != '[':
            print(0)
            exit(0)
        
        elif n[i-1] == '[': 
            res += num
        stk.pop()
        num //= 3
            
        
        
if stk:
    print(0)
else:
    print(res)
