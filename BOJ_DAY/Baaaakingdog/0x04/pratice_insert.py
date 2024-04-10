

mx = 10005
dat = [0] * mx
pre = [-1] * mx
nxt = [-1] * mx
unused = 1

def travers():
    cur = nxt[0]
    while (nxt[cur] != -1):
        print(dat[cur], end = " ")
        cur = nxt[cur]

def insert(addr,num):
    global unused
    
    dat[unused] = num
    pre[unused] = addr
    nxt[unused] = nxt[addr]
    
    if nxt[addr] != -1:
        pre[nxt[addr]] = unused
    nxt[addr] = unused
    unused += 1 
    
def erase(addr):
    nxt[pre[addr]] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = pre[addr]
