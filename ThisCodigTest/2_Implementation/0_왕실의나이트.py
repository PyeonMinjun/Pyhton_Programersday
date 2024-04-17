
n = input()
t = ['a','b','c','d','e','f','g','h']

x = int(n[1]) - 1
y = n[0]

for i in range(len(t)):
    if y == t[i]:
        y = i
        

dx = [2,-2,1,-1,2,-2,1,-1]
dy = [1,1,2,2,-1,-1,-2,-2]

cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
        continue
    else:
        cnt += 1
print(cnt)
    