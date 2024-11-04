# 맨해튼 + dfs로 해결하기 + 연결리스트.
def dfs(abj,check,cur):
    check[cur] = True
    for n_node in abj[cur]:
        if not check[n_node]:
            dfs(abj,check,n_node)

t = int(input())
for _ in range(t):
    n = int(input())

    location = []
    for _ in range(n+2):
        location.append(list(map(int,input().split())))

    abj = [[] for _ in range(n+2)]

    for i in range(n+2):
        for j in range(i+1, n+2):
            if abs(location[i][0]- location[j][0]) + abs(location[i][1] - location[j][1]) <= 1000:
                abj[i].append(j)
                abj[j].append(i)

    
    # dfs 돌기 
    check = [False] * (n+2)
    dfs(abj,check,0)


    if check[n+1]:
        print("happy")
    else:
        print("cry")



    









    
    

    

