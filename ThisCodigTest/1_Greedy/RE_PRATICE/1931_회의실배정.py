# from operator import itemgetter
# n = int(input())
# ns = [list(map(int,input().split())) for _ in range(n)]

# ns.sort()
# ns.sort(key = itemgetter(1))

# cnt = 1
# time = ns[0][1]


# for t in ns[1:]:
#     if t[0] >= time:
#         time = t[1]
#         cnt += 1

# print(cnt)

# dp

N = int(input())
meetings = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))

print(meetings)

dp = [0 for _ in range(N)]
dp[0] = 1

for i in range(1, N):
    meetings_i = []
    
    for j in range(i):
        if meetings[j][1] <= meetings[i][0]:
            meetings_i.append(dp[j])
            
    if meetings_i:
        dp[i] = max(meetings_i) + 1
    else:
        dp[i] = 1

print(max(dp))

