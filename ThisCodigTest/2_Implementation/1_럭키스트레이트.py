n = (input())

k = len(n)

n_left = n[:k//2] 
n_right = n[k//2:]

left_res = 0
right_res = 0

for i in n_left:
    left_res += int(i)

for i in n_right:
    right_res += int(i)   
    
if left_res == right_res:
    print("LUCKY")
else:
    print("READY")

