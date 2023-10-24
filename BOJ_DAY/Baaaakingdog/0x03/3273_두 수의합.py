n = int(input())
ns = list(map(int, input().split()))
x = int(input())

cnt =0

# for i in range(n):
#     for j in range(i+1,n):
#         if ns[i] + ns[j] == x:
#             cnt += 1

# print(cnt)

arr = [0] * 2000001

for i in ns:
    arr[i] += 1

    if arr[x-i]:
        cnt += 1

print(cnt)