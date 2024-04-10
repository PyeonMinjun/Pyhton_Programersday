n = int(input())

for i in range(1,n+1):
    st = (input())
    
    for k in range(1,10):
        if st[:k] == st[k:k*2]: 
            print("#{} {}" .format(i,k))           
            break