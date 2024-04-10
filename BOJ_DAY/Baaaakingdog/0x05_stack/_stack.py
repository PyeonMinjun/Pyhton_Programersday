mx = 10
dat = [0] * mx
pos = 0


def push(x):
    global pos
    
    dat[pos] = x
    pos += 1
    
    
def pop():
    global pos
    pos -= 1
    
def top():
    global pos
    return(dat[pos-1])

push(12)
print(dat)

pop()
print(dat)
push(8)
print(dat)

print(top())

