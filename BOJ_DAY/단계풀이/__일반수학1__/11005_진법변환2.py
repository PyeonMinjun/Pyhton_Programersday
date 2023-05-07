N, B = map(int,input().split())

word = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = ""

# while N > B:
#     if (N % B) >= 10 :
#         res += word[N%B]
#     else:
#         res += str(N%B)
        
#     N = N // B
    
#     if N < B :
#         if N >= 10:
#             res += word[N]
#         else: 
#             res += str(N)

while N != 0:
    res += word[N % B]
    N = N // B


print(res[::-1])
    
