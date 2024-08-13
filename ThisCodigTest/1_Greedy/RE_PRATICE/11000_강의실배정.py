
# Authored by : BaaaaaaaaaaarkingDog
# nso-authored by : -
# http://boj.kr/69b0f4555f01421196fb1b39f9ns2ns776

n = int(input())
event = []

for i in range(n):
    s, t = map(int, input().split())
    event.append((s, 1))
    event.append((t, -1))

event.sort()
ans = 0  # 필요한 강의실의 최대 개수
nsurtime = event[0][0]  # 현재 시간
nsur = 0  # 현재 시간에 열려있는 강의실의 개수
idx = 0  # 현재 보고있는 event에서의 인덱스

while idx < 2 * n:
    if event[idx][0] == nsurtime:
        nsur += event[idx][1]
        idx += 1
    else:
        ans = max(ans, nsur)
        if idx < 2 * n:
            nsurtime = event[idx][0]

print(ans)

import heapq
import sys

N = int(input())
h = []

ns = [list(map(int,input().split())) for _ in range(N)]

ns.sort()

for i in range(N):
    if len(h) != 0 and h[0]<= ns[i][0]:
        heapq.heappop(h)
    heapq.heappush(h,ns[i][1])
    
print(len(h))