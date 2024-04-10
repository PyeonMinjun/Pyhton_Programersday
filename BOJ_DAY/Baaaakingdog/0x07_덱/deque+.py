mx = 100005
dat = [0] * ((2*mx)+1)

head = mx
tail = mx

def push_front(x):
    global head

    head -= 1
    dat[head] = x
    
def push_back(x):
    global tail

    dat[tail] = x
    tail +=1
    

def pop_front():
    global head
    head +=1 
    
def pop_back():
    global tail
    tail -= 1
    
def front():
    return dat[head]

def back():
    return dat[tail-1]


push_back(30)
print(front())
push_front(25)
push_back(12)
print(back())
push_back(62)
pop_front()
print(front())
pop_front()
print(back())
