# n= []
# for _ in range(3):
#     n.append(int(input()))

# mult = 1
# for i in n:
#     mult *=i

# res = list("".join(str(mult)))

# arr = [0] * 10
# for i in res:
#     i = int(i)
#     arr[i] += 1
    
# for i in arr:
#     print(i)
    
# ----------------------------------------------2번째풀이
a = (int(input()))
b = (int(input()))
c = (int(input()))
    
res= list(str(a*b*c))

for i in range(10):
    print(res.count(str(i)))