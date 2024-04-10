import sys
input = sys.stdin.readline

n = int(input())

stk = []
res = []
temp = []
cnt = 0


for _ in range(n):
    ns = int(input())
    while not stk or stk[-1] != ns:
        if cnt > ns:
            print("NO")
            exit(0)  
        cnt += 1
        stk.append(cnt)
        temp.append("+")
    
    else:
        stk.pop()
        temp.append("-")
print(temp)