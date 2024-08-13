# O(N^2) 풀이

n = int(input())
ns = [int(input()) for _ in range(n)]

max_cnt = 0
res = 0

for i in range(n):
    cnt = ns.count(ns[i])
    if cnt > max_cnt or (cnt == max_cnt and res < ns[i]):
        max_cnt = cnt
        res = ns[i]
        
print(res)