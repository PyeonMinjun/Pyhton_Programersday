t = int(input())

for tc in range(t,t+1):
    ns = (input())
    ans = ""
    
    for i in ns:
        ans += i
        if ans[:len(ans)//2] == ans[len(ans)//2:]:
            t = ans[:len(ans)//2]
            print("#{} {}" .format(tc,t) )
            