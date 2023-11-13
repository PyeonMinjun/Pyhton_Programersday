t = int(input())

# 대문자 65
# 소문자 97

for i in range(1,t+1):
    ns = input()
    ans = ""
    for i in ns:
        ans += i
        if ans[:len(ans)//2] == ans[len(ans)//2:]:
            break
    print(ans[:len(ans)//2])
    

for i in range(1,t+1):
    ns = input()
    
    for i in range(10):
        patten = ns[:i]
        new_patten = ns[i:i*2]
        if patten == new_patten:
            break
    print(patten)
    