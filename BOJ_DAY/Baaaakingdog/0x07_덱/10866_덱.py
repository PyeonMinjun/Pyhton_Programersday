n = int(input())

mx = 10001
dat = [0] *((mx *2) +1)

head = mx
tail = mx

def push_front(x):
    global head
    head -= 1
    dat[head] = x

def push_back(x):
    global tail
    
    dat[tail] = x
    tail += 1
    
def pop_front():
    global head
    if tail - head == 0:
        return -1
    
    head += 1
    return dat[head-1]

def pop_back():
    global tail
    if tail - head == 0:
        return -1
    
    tail -= 1
    return dat[tail]

def size():
    return tail - head

def empty():
    if tail - head == 0:
        return 1
    else:
        return 0
    
def front():
    if tail - head == 0:
        return -1
    return dat[head]

def back():
    if tail - head == 0:
        return -1
    return dat[tail-1]
        
    
        
    

for i in range(n):
    ns = list(input().split())
    if ns[0] == "push_front":
        push_front(ns[1])
        
    elif ns[0] == "push_back":
        push_back(ns[1])
    elif ns[0] == "pop_front":
        print(pop_front())
    elif ns[0] == "pop_back":
        print(pop_back())
    elif ns[0] == "size":
        print(size())
    elif ns[0] == "empty":
        print(empty())
    elif ns[0] == "front":
        print(front())
    else:
        print(back())
        
    
    
