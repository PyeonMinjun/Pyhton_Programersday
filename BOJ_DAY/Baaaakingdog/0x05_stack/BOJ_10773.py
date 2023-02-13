import sys


input = sys.stdin.readline
n = int(input())

arr = []
for i in range(n):
    
    ns = int(input())    
    if not ns:
        arr.pop()
    else:
        arr.append(ns)     
    

print(sum(arr))