n, m = map(int,input().split())

text = (input())
text = list((''.join(text)))


arr = [0] * len(text)

cnt = -1
for i in text:
    cnt += 1
    if i == 'e':
       arr[cnt] = 1 # [0,1,1]

for i in range(m):
    L,R= map(int,input().split()) 
    e_cnt = arr[L-1:R]
    # print(e_cnt)
    print(e_cnt.count(1))