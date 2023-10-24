import sys
input = sys.stdin.readline




mx = 600001
dat = [''] * mx
pre = [-1] * mx
nxt = [-1] * mx

unused = 1


def traverse():
    cur = nxt[0]
    while cur != -1:
        print(dat[cur], end ="")
        cur = nxt[cur]
    
def insert(addr, num):
    global unused
    
    dat[unused] = num
    pre[unused] = addr
    nxt[unused] = nxt[addr]
    
    if nxt[addr] != -1:
        pre[nxt[addr]] = unused
    nxt[addr] = unused
    unused += 1

def erase(addr):
    global unused
    
    nxt[pre[addr]] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = pre[addr]
        
    
        


n = input().rstrip()
m = int(input())

cursor = 0
for i in n:
    insert(cursor,i) # 1 a
    cursor += 1
    
for i in range(m):
    op = input()
    
    if op[0] == "P":
        insert(cursor,op[2])
        cursor = nxt[cursor]
    
    if op[0] == "L":
        if pre[cursor] != -1 :
            cursor = pre[cursor]
    
    if op[0] == "D":
        if nxt[cursor] != -1 :
            cursor = nxt[cursor]
        
    if op[0] == "B":
        if pre[cursor] != -1:
            erase(cursor)
            cursor = pre[cursor]
        
traverse()
        
        
        
