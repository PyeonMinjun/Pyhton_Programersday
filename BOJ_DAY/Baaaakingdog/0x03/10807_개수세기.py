n = int(input())
ns = map(int,input().split())
v = int(input())

arr = [0] * 201

for i in ns:
    if i < 0 :
        arr[abs(i)+100] += 1
    else:
        arr[i]+= 1


if v >= 0:
    print(arr[v])
else:
    print(arr[abs(v)+100])
    