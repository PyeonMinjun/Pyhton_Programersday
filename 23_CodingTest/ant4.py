t  = int(input())

for _ in range(t):
    len , wall = map(int,input().split()) 
    s = input()                           
    cnt = 0
    x = s.find("@")
    y = s.find("O")
    Oarr = []
    Ocnt = 0

    for i in s:
        if i == "O":
            Ocnt += 1
            Oarr.append(Ocnt)


    j_a, j_hp = map(int,input().split()) #사람 공격력 / 체력    
    m_a, m_hp = map(int,input().split()) #몬스터 공격력 / 체력 

    
    if x < y:
        result = s[x:y]
    elif x > y:
        x ,y = y,x
        result = s[x:y]


    for f in result:
        if f == "#":
            cnt += 1
        if f == "&":
            while m_hp <= 0 or j_hp <=0: 
                m_hp -= j_a
                j_hp -= m_a
                

                if m_hp <= 0:
                    continue
                if j_hp <= 0:
                    print("HELP!")
                    exit(0)

    if (cnt <= wall):
        print("HAHA!")
    else:
        print("HELP!")

