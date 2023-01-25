t = int(input())
s_list = []
s_sec = []
ans = []
ran = [0]

for _ in range(t):
    s_list.append(input())

for _ in range(t):
    s_sec.append(int(input()))


qt_cnt= int(input())

for _ in range(qt_cnt):
    ans.append(int(input()))


# print(s_list,s_sec,qt,ans)
# 1초부터 180초까지는 b1 / 181초부터 (180 + 178) 까지 b2
# 0 1 /1 2/ 2 3 /3 4 

#  ans = 물어보는 초
k = 0
for i in range(len(s_sec)):
    k += s_sec[i]
    ran.append(k)

print(ran)



for x in ans:
    cnt = 0
    for c1,c2 in zip(ran,ran[1:]):
        if c1+1 <= x <= c2:
            print(s_list[cnt])
            break
        else:
            cnt += 1

            
        
        
