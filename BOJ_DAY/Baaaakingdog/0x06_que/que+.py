mx = 10005
dat = [0] * mx
head, tail = 0,0


def push(x):
    global tail
    dat[tail] = x
    tail += 1

def pop():
    global head
    head += 1

def front():
    return dat[head]

def back():
    return dat[tail-1]