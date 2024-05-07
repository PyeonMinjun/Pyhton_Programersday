from operator import itemgetter
n = int(input())

time = [list(map(int,input().split())) for _ in range(n)]

time.sort()
time.sort(key = itemgetter(1))
cnt = 1


start = time[0][0]
end = time[0][1]

for val in time[1:]:
    if end > val[0]:
        continue
    else:
        start = val[0]
        end = val[1]
        cnt += 1

print(cnt)
    
    