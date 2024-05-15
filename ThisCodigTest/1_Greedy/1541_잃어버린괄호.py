tmp, ans = 0, 0
sign = 1

input_str = input()
for c in input_str:
    if c == '+' or c == '-':
        ans += tmp * sign
        if c == '-':
            sign = -1
        tmp = 0
    else:
        tmp = tmp * 10 + int(c)

ans += tmp * sign
print(ans)
