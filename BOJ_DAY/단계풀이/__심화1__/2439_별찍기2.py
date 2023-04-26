n = int(input())
# 1)
# cnt = 1

# for i in range(n-1,-1,-1):
#     o = " " * i
#     print(o+ "*" * cnt)
#     cnt += 1

# 2)

for i in range(1,n+1): # 1 2 3 4 5
    print(" "*(n-i) + "*" * i)