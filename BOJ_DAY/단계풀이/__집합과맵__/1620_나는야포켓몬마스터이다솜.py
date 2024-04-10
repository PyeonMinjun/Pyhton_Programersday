import sys
input = sys.stdin.readline
n,m = map(int,input().split())

ns = {}

for i in range(1, n+1):
    a = input().rstrip()
    ns[i] = a
    ns[a] = i
    

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(ns[int(quest)])
    else:
        print(ns[quest])
    
        