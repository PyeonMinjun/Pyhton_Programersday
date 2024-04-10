n = (input())
m = int(n)
length = int(len(list("".join(n))))
ninelen = (9 * length)
arr = [] 

for i in range(1,ninelen+1):
  dis  = (m - i)  
  if dis > 0:
    if i == sum(map(int,str(dis))):
        arr.append(dis)
      
      
if arr:
    print(min(arr))
else:
    print(0)