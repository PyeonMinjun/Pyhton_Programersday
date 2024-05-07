
def func1(a,b,n):
    if n == 1:
        print(a,b)
        return 
    
    func1(a,6-a-b,n-1)
    func1(a,b,1)
    func1(6-a-b,b,n-1)
    
    
k = int(input())
print(2**k-1)
func1(1,3,k)
    
    