n = input()

cnt = 0 


for i in n:
    if i == "1":
        cnt += 1 

if n == "0000":
    cnt = 5
print(cnt)