# import sys
# input = sys.stdin.readline
t = int(input())


for _ in range(t):
    order = input()#.strip()
    os = int(input())#.strip())
    ns = input()[1:-1].split(",")
            
        

    mx = 10
    dat = [0] * ((mx*2)+1)
    head = mx
    tail = mx+os
    flag = 0
    cnt = 0
    rev = 0
    
    for i in ns:
        dat[mx+cnt] = i
        cnt += 1
    
    for i in order:
            if i == "R":
                rev += 1

            else:
                if ns:
                    if tail - head == 0 or os == 0:
                        flag = 1                
                    
                    if rev % 2 == 0:
                        head += 1
                        dat[head-1] = 0
                        
                    else:
                        tail -= 1
                        dat[tail] = 0
                else:
                    flag = 1
               
    
    arr= []
    for i in dat:
        if i == 0:
            continue
        else:
            arr.append((i))
            
    if flag:
        print("error")
    else:
        if rev % 2 == 0:
            print("[{}]" .format( ",".join(map(str,arr))))
        else:
            
            arr.reverse()
            print("[{}]" .format( ",".join(map(str,arr))))
            
            
    