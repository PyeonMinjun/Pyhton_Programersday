a =  input()
b =  input()
arr1 = [0] * 27
arr2 = [0] * 27
na = ''.join(a)
nb = ''.join(b)

cnt = 0

for i in na:
    arr1[ord(i)-97] +=1

for i in nb:
    arr2[ord(i)-97] +=1
        

for i in range(27):
    cnt += abs(arr1[i] - arr2[i])
    
print(cnt)