import sys

input = sys.stdin.readline

n = int(input())

arr = {}


for i in range(n):
    name, rec = (input().split())
    if rec == "enter":
        arr[name]= "enter"
    
    else:
        if arr[name]:
            del arr[name]

for i in sorted(arr, reverse=True):
    print(i)
    
    
        