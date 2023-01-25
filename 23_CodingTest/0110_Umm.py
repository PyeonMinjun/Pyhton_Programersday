t = int(input())

for _ in range(t):
    s_cnt = int(input())
    s = input()
    m,n = map(int, input().split())

    res = s[m-1:n]
    ad_m = "m"
    
    for _ in range(s_cnt):
        if res == "Um" + ad_m:
            print("YES")
            break
        ad_m += "m"

    else:
        print("NO")