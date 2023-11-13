t = int(input())

for tc in range(1,t+1):
    P,Q,R,S,W = list(map(int,input().split()))
    
    A_cp = W * P
    B_cp = 0
    
    if Q:
        if W <= R:
            B_cp = Q
        else:
            cost = W - R
            B_cp = Q + (cost * S)

    if A_cp < B_cp:
        print("#{} {}" .format(tc,A_cp))
    else:
        print("#{} {}" .format(tc,B_cp))

    