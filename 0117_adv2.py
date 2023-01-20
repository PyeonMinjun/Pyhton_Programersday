t = int(input())
for _ in range(t):
    n, m = map(int,input().split()) #세로 가로
    map1 = []
    damage = 0

    for _ in range(n):
        x1 = input()
        map1.append(x1)

    c = 0
    for i in map1:
        map1[c]= list(i)
        c +=1
    
    move_t = int(input())
    move_v = input()

    for i in range(n):
        for j in range(m):
                if map1[i][j] == '@':
                    y,x = i,j
                    
    for i in move_v:
        if i == "R":
            if x+1 >= m:
                if map1[y][x] == '^':
                    damage += 1
                continue
            if map1[y][x+1] == "#":
                if x == '^':
                    damage += 1
                continue
            else:
                if map1[y][x+1] == '^':
                    damage += 1
                    map1[y][x+1] = '@'
                    map1[y][x] = '.'
                    x+= 1

                else:
                    map1[y][x] , map1[y][x+1] = map1[y][x+1] , map1[y][x]
                    x+= 1

            print("R",map1,damage)
        elif i== "L":
            if x-1 < 0:
                if x == '^':
                    damage += 1
                continue
            if map1[y][x-1] == "#":
                if x == '^':
                    damage += 1
                continue 
            else:
                map1[y][x] , map1[y][x-1] = map1[y][x-1] , map1[y][x] 
                x -= 1
                # print("L",map1)

        elif i == "U" :
            if y-1 < 0:
                continue
            if map1[y-1][x] == "#" :
                continue
            else:
                map1[y][x] , map1[y-1][x] = map1[y-1][x] , map1[y][x]
                y-=1
                # print("U",map1)

        elif i == "D" :
            if y+1 >= n:
                continue
            if map1[y+1][x] == "#" :
                continue
            else:
                map1[y][x] , map1[y+1][x] = map1[y+1][x] , map1[y][x]
                y+=1
                # print("D",map1)


    for i in range(n):
        for j in range(m):
                if map1[i][j] == '@':
                    y,x = i,j
    
    print(y+1 ,x+1)