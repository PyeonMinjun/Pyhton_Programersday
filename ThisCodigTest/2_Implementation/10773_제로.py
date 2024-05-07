k = int(input())

arr = []

for _ in range(k):
    n = int(input())
    
    if not n:
        arr.pop()
    else:
        arr.append(n)
    
print(sum(arr))