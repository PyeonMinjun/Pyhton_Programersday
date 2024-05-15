n = input()

tmp = 0
ans = 0
sign = 1

for i in n:
    if i == '-' or i == '+':
        ans += tmp * sign
        if i == '-':
            sign = -1
        tmp = 0
    else:
        tmp = tmp * 10 + int(i)

ans += tmp * sign

print(ans)
        
    