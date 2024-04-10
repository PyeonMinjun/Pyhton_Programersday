import sys
input = sys.stdin.readline


dat =[0] * 100001
pos = 0
def push(x):
    global pos
    
    dat[pos] = x
    pos += 1

def pop():
    global pos
    if not pos:
        return -1
    pos -= 1
    return dat[pos]
    

def size():
    return pos

def empty():
    if pos:
        return 0
    return 1

def top():
    if not pos:
        return -1
    
    return dat[pos-1]


n = int(input())

for i in range(n):
    o = input().split()
    if o[0] == "push":
        push(o[1])
    elif o[0] == "pop":
        print(pop())
    elif o[0] == "size":
        print(size())
    elif o[0] == "empty":
        print(empty())
    elif o[0] == "top":
        print(top())