n = int(input())

dat = [0] * 1000001
cnt = 1
head = 0
tail = n

for i in range(n):
    dat[i] =cnt
    cnt += 1

while tail - head != 1:
    head += 2
    dat[tail] = dat[head-1]
    tail += 1
    

res2 = {0}

dat = [i for i in dat if i not in res2]
print(dat[-1])
