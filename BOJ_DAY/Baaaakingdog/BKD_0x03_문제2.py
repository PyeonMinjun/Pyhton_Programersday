# n = int(input())
# ns = list(map(int,input().split()))

# for i in range(n):
#     for j in range(i+1,n):
#         if (ns[i] + ns[j]) == 100:
#             print(1)
#             exit(0)        
# else:
#     print(0)


# 시간복잡도 O(n) 효율성
n = int(input())
ns = list(map(int,input().split()))

arr = [0] * 101
for i in ns:
    if arr[100 - i]:
        print(1)
        break
    else:
        arr[i] = 1
    
    print(arr)
else:
    print(0)
        
     