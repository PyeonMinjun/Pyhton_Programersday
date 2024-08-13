n = int(input())

AS = list(map(int,input().split()))
BS = list(map(int,input().split()))

AS.sort()
BS.sort(reverse= True)

s= 0

for i in range(n):
    s += AS[i] * BS[i]

print(s)
    
    
