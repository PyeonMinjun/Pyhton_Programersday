n = (input())

cnt = [0,0]

if n[0] == '0':
    cnt[0] += 1
else:
    cnt[1] += 1

for i in range(1,len(n)):
    if n[i] != n[i-1]:
        cnt[int(n[i])] += 1

print(min(cnt[0],cnt[1]))