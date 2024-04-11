n = input()

zeroCnt = 0
oneCnt = 0

if n[0] == '0':
    zeroCnt += 1
    
else:
    oneCnt += 1
    
for i in range(len(n)-1):
    if n[i] != n[i+1]:
        if n[i+1] == '0':
            zeroCnt += 1
        elif n[i+1] == '1':
            oneCnt += 1
print(zeroCnt,oneCnt)
print(min(oneCnt,zeroCnt))
        
    

