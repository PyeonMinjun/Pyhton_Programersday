n = int(input())

# cnt = 0
# for i in range((2*n)-1,-1,-2):
#     print(" "* cnt + "*" * i)
#     cnt += 1
    

for i in range(n,0,-1):
    print(" " * (n-i) + "*" * (2*i-1))