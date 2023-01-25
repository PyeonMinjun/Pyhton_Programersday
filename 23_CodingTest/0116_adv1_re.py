t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    
    k= {
        "R":[0, 1],
        "L":[0,-1],
        "U":[-1,0],
        "D":[1,0]
    }

    arr = []
    for _ in range(n):
        arr.append(input())
    
    bin = []
    for i in arr:
        bin.append(list(i))

    for i in range(n):
        for j in range(m):
            if bin[i][j] == "@":
                x,y = j,i

    n = int(input())
    n_code = input()

    for c in n_code:
        dx = x + k[c][0]
        dy = y + k[c][1] 

    if dx >= 0 and dx <n and 0 <= dy and dy <= m and bin[dy][dx] != '#':
        x = dx
        y = dy 