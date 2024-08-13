n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort()

# res = []
ans = 0
for i in range(1,n+1):
    # res.append(rope[n-i]* i)
    ans = max(ans, rope[n-i]* i)
    
print(ans)
    
    