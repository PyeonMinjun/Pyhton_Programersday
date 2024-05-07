n = int(input())
cnt = n

for _ in range(n):
    data = input()
    for j in range(len(data)-1):
        
        if data[j] != data[j+1]:
            if data[j] in data[j+1:]:
                cnt -=1
                break

print(cnt)
    
    
    