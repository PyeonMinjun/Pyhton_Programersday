N, K = map(int, input().split())

pre = [0] * 5001
nxt = [0] * 5001
v = []

# 원형 연결 리스트 생성
# 맨 처음 노드와 마지막 노드가 서로를 가리키도록 지정
for i in range(1, N + 1):
    pre[i] = N if i == 1 else i - 1
    nxt[i] = 1 if i == N else i + 1

len = N
i = 1
cur = 1

# 연결 리스트를 순회하며 순열 생성
while len != 0:
    # K 번째일 때 제거
    if i == K:
        pre[nxt[cur]] = pre[cur]
        nxt[pre[cur]] = nxt[cur]
        v.append(cur)
        i = 1
        len -= 1
    else:
        i += 1
    cur = nxt[cur]

# 요세푸스 순열 출력
result = ", ".join(map(str, v))
print(f"<{result}>")
