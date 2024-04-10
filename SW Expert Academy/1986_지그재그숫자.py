t = int(input())

for tc in range(1, t+1):
    ns = (int(input()))
    total = 0
    for i in range(1,ns+1):
        if i % 2 == 0:
            total -= i
        else:
            total += i
    
    print("#{} {}" .format(tc , total))