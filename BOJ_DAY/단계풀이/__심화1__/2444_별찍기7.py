n = int(input())

# cnt = 1
# for i in range(n-1,-1,-1):
#     print(" "* i + "*" * cnt)
#     cnt += 2

# cnt -= 4
# for j in range(1,n):
#     print(" "* j+ "*"* cnt )
#     cnt -= 2 

for i in range(1,n):
    print(" "*(n-i) + "*" *(2*i-1))

for i in range(n,0,-1):
    print(" "* (n-i) + "*" * (2*i-1) )
    
    



# 4 3 2 1 0 1 2 3 4  빈공간

# 1 3 5 7 9 7 5 3 1
#     *
#    ***
#   *****
#  *******
# ********* 9
#  *******
#   *****
#    ***
#     *