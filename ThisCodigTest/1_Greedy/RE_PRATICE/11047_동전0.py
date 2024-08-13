n,m = map(int,input().split())
coin = [int(input()) for _ in range(n)]
cnt= 0
coin.sort()

for i in coin[::-1]:
    if m >= i:
        cnt += m // i
        m %= i
print(cnt)
        