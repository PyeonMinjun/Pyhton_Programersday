arr = [0]* 50001


for i in range(1,20001):
    n = 0
    n  += i
    
    while i:
        k = i // 10
        n += i % 10
        i //= 10
    arr[n] += 1

for i in range(1, 10001):
    if not arr[i]:
        print(i)

    
    