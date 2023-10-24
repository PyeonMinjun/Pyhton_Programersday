



def traverse():
    cur = nxt[0]
    while cur != -1:
        print(dat[cur], end ="")
        cur = nxt[cur]
        
def insert(addr, num):
    global non
    
    dat[non] = num
    pre[non] = addr
    nxt[non] = nxt[addr]
    
    if nxt[non] != -1:
        pre[nxt[non]] = non
    nxt[pre[non]] = non
    non += 1

def erase(addr):
    global non
    
    if nxt[addr] != -1:
        pre[nxt[addr]] = pre[addr]
    nxt[pre[addr]] = nxt[addr]



n = int(input())
for _ in range(n):
    mx = 1000001
    dat = ['']* mx
    pre = [-1]* mx
    nxt = [-1]* mx

    non = 1
    
    m = input()
    cursor = 0
    
    for i in m:
        if i == "<":
            if pre[cursor] != -1:
                cursor = pre[cursor]
        elif i == ">":
            if nxt[cursor] != -1:
                cursor = nxt[cursor]
        
        elif i == "-":
            if pre[cursor] != -1:
                erase(cursor)
                cursor = pre[cursor]
        else:
            # if nxt[cursor] != -1:
                insert(cursor,i)
                cursor = nxt[cursor]
    
    traverse()
    print()

     