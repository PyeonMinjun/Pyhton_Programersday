n = int(input())

ns = list(map(int,input().split()))
ns.sort()

print(ns[n//2])