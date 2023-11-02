import sys
input = sys.stdin.readline

n,m  = list(map(int,input().split()))
ns = list(map(int,input().split()))

mx = 101
dat = [0] * ((mx*2) +1)

head = mx
tail = mx+n

for i in range(1,n+1):
    dat[mx+i-1] = i

cnt = 0


for i in ns:
    if dat[head] != i:
        if dat.index(i) - head > (tail - dat.index(i)):
            while dat[head] != i:
                tail -= 1
                head -= 1
                dat[head] = dat[tail]
                dat[tail] = 0
                cnt += 1
            else:
                head += 1
        else:
            while dat[head] != i: 
                head += 1
                tail += 1
                dat[tail-1] = dat[head-1]
                dat[head-1] = 0
                cnt += 1
            else:
                head += 1
    else:
        head += 1
    
            
print(cnt)