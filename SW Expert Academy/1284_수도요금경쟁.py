t = int(input())
# a = 1L  : 8 p원
# b = 100L r  : 300 q원   100L이상사용시 1리터당 10 S원
# 종민이 250 리터사용

for i in range(1,t+1):
    P,Q,R,S,W = map(int,input().split())  # 8 300 100 10 250
    
    if W <= R:
        res = Q
    elif W > R:
        res = Q + ((W-R) * S)
    
    if res > (P * W):
        total = P*W
    elif res < (P * W):
        total = res
        
    print("#{} {}" .format(i, total))     
    