data = input()
res = []
cnt = 0

for i in data:
    if i.isalpha():
        res.append(i)
    else:
        cnt += int(i)
        
res.sort()

print("".join(res) + str(cnt))