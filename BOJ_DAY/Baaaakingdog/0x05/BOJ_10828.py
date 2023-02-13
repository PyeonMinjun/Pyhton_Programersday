import sys
n = int(input())

stk = []
input = sys.stdin.readline

for i in range(n):
    bin = []
    bin = (input().split())
    a = bin[0]
    # 밑에 함수들도 bin[0]으로 작성하면될듯
        
        
    
    if bin[0] == 'push':
        stk.append(bin[1])
       
    
    elif a == "top":
        if stk:
            print(stk[-1])
        else:
            print(-1)
        
    elif a == "size":
        print(len(stk))
    
    elif a == "empty":
        if stk:
            print(0)
        else:
            print(1)
    
    elif a == "pop":
        if stk:
            p = stk.pop()
            print(p)
        else:
            print(-1)

    # print(stk)
    