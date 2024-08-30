n = int(input())
arr = []
cnt=  0

def dfs(depth):
    if depth == n:
        global cnt
        idx = 0
        # is_used = False
        while idx < n:
            if idx + arr[idx] > n:
                return
            for i in range(idx, idx+arr[idx]):
                if arr[idx] != arr[i]:
                    return
                
            idx += arr[idx]
            
        cnt +=1
        return
    
    for i in range(1,5):
        arr.append(i)
        dfs(depth+1)
        arr.pop()

dfs(0)
print(cnt)


