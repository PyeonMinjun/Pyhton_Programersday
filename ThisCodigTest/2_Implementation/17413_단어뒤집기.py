ns = input() + ' '

stk = []
res = ''
side = 0


for i in ns:
    if i == '<':
        side = 1
        for _ in range(len(stk)):
            res += stk.pop()
    
    stk.append(i)
    
    if i == '>':
        side = 0
        for _ in range(len(stk)):
            res += stk.pop(0)
    
    if side == 0 and i == ' ':
        stk.pop()
        for _ in range(len(stk)):
 
            res += stk.pop()
        res += ' '
            
print(res)


                
        
            
            
            