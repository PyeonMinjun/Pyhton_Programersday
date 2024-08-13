n = input()

tmp = ''
res = 0
sign = 1

for s in n:
    if s == '-' or s == '+':
        res += int(tmp) * sign
        if s == '-':
            sign = -1
        tmp = ''  
        
    else:
       tmp += s 
res += int(tmp) * sign

print(res)
    