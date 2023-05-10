x,y,w,h = map(int,input().split())

dix = w-x
diy = h-y

print(min(dix,diy,x,y))