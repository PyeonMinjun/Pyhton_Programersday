n = int(input())
ns= map(int,input().split())

def sieve(n):
    isprime =[True] * (n+1)
    isprime[0] = isprime[1] = False
    sn = int(n ** 0.5)
    
    for i in range(2, sn+1):
        if isprime:
            for j in range(i*2,n+1,i):
                isprime[j] = False
    return isprime

isprime = sieve(1000)
result = 0

for i in ns:
    if isprime[i]:
        result += 1

print(result)
    
    
    
    