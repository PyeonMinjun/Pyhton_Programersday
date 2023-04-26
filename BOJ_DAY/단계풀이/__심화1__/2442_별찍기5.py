n = int(input())
# cnt = 1 
# for i in range(n-1,-1,-1):
#     o = " " * i
#     star = "*" * cnt
#     print(o+star)
    
#     cnt += 2
    
    
    
# 2)

for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))