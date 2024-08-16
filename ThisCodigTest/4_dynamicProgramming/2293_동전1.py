n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]

d= [0] * (k+1)
d[0] = 1

for coin in coins: # 1, 2, 5
    for i in range(coin,k+1):
        d[i] += d[i-coin]

print(d[k])