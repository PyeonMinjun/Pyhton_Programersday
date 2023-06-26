n,m = map(int,input().split())

arr = []
count = []

for i in range(n):
    arr.append(input())



for a in range(n-7): # 0~2 
    for b in range(m-7): # 0~5
        indexW = 0
        indexB = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j) % 2 == 0:
                    if arr[i][j] != "B":
                        indexW += 1
                    elif arr[i][j] != "W":
                        indexB += 1
                else:
                    if arr[i][j] != "B":
                        indexB += 1
                    elif arr[i][j] != "W":
                        indexW += 1
        count.append(min(indexW,indexB))
print(count)
print(min(count))
                    
    