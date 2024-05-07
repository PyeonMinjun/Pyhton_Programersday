n, m = map(int,input().split())
coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)
cnt = 0 
for i in coins:
    if  i <= m:
        cnt += m // i
        m = m % i

print(cnt)