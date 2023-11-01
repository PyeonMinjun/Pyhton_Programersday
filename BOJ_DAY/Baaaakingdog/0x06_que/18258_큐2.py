import sys

input = sys.stdin.readline

n= int(input())

mx = 2000001
dat = [0] * mx
head = 0
tail = 0 

def push(x):
    global tail 
    
    dat[tail] = x
    tail += 1

def pop():
    global head
    
    if tail - head == 0:
        return -1
    else:
        head += 1
        return(dat[head-1])
    
def size():
    return tail - head

def empty():
    
    if tail - head == 0:
        return 1
    else:
        return 0
    
def front():
    global head
    if tail - head == 0:
        return -1
    else:
        return dat[head]

def back():
    global tail
    
    if tail - head == 0:
        return -1
    
    else:
        return dat[tail-1]
    
    




for i in range(n):
    ns = list(input().split())
    
    if ns[0] == "push":
        push(ns[1])
    elif ns[0] == "pop":
        print(pop())
    elif ns[0] == "size":
        print(size())  
    elif ns[0] == "empty":
        print(empty())
    elif ns[0] == "front":
        print(front())
    elif ns[0] == "back":
        print(back())
        
    
    