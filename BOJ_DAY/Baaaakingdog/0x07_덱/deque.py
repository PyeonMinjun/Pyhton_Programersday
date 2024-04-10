mx = 10005
dat = [0] * (mx+1)
head = mx
tail = mx

def push_front(x):
    dat[head] = x
    head = head - 1
    
def pop_front():
    head = head + 1

def pop_back():
    tail = tail -1
    
def front():
    return dat[head]

def back():
    return dat[tail-1]
