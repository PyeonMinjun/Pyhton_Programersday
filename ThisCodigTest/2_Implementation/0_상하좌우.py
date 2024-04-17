n = int(input())
nss = list(input().split())

dx = [0,0,-1,1]
dy =  [1,-1,0,0]
data =  ["R","L","U","D"]
x,y = 0, 0

for ns in nss:
    for i in range(len(data)):
        if ns == data[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
    
    x,y = nx,ny
    
print(x+1,y+1)            