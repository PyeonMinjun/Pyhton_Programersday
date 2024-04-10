import sys
input = sys.stdin.readline

n,m= map(int,input().split())

ns = set(map(int,input().split()))
ms = set(map(int,input().split()))

print(len(ns-ms) + len(ms-ns))
