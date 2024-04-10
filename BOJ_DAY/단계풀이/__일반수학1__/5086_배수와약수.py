
while True:
    n,m = map(int,input().split())
    
    if n < m:
        for i in range(1,10001):
            if m == n * i:
                print('factor')
                break
        else: 
            print('neither')
            
    elif n > m:
        for i in range(1,10001):
            if n  == m * i:
                print('multiple')
                break
        else: 
            print('neither')
            
    
    
    if n == 0 & m == 0:
        break 