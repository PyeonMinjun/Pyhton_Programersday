mx = 10005
dat = [0] * mx
head = 0
tail = 0


def push(x):
    global tail
    dat[tail] = x
    tail = tail + 1

def pop():
    global head
    head = head + 1

def front():
    return dat[head]

def back():
    return dat[tail-1]


push(3)
push(4)
push(5)
pop()
print(dat)

print(front())
print(back())


