n = int(input())


for i in range(n):
    m = int(input())
    # 25 10 5 1
    q = 0
    d = 0
    ni = 0
    p = 0    
    
    if m >= 25:
        q += m // 25
        m %= 25
    
    if 25 > m >= 10:
        d += m // 10
        m %= 10 
        
    if 10 > m >= 5:
        ni += m // 5
        m %= 5
    
    if 5 > m >= 1:
        p += m // 1
        m %= 1

    print(q,d,ni,p)