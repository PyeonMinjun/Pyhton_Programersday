ns = input() + ' '

stk = []
res = ''
check = 0 

for i in ns:
    
    if i == '<':
        check = 1
        while stk:
            res += (stk.pop())
            
    stk.append(i)
    
    if i == '>':
        check = 0
        while stk:
            res += stk.pop(0)
    
    if check == 0 and i == ' ':
        stk.pop()
        while stk:
            res += stk.pop()
        res += ' '
print(res)
            
    
        
        