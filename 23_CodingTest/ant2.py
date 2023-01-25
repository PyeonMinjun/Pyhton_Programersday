t  = int(input())

for _ in range(t):
    len , wall = map(int,input().split()) # len = 길이(7) / wall = 벽부수기 횟수
    s = input()                           # @ = 준식 / 0 = 탈출구 / G = 건틀렛 /  . = 빈칸 / # = 벽
    cnt = 0
    x = s.find("@")
    y = s.find("O")

    if x < y:
        result = s[x:y]
    elif x > y:
        x ,y = y,x
        result = s[x:y]


    for f in result:
        if f == "#":
            cnt += 1

    if (cnt <= wall):
        print("HAHA!")
    else:
        print("HELP!")

