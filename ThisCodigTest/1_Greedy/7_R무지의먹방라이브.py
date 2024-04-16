from operator import itemgetter

def solutuion(food_times,k):
    arr = []
    n = len(food_times)
    for i in range(n):
        arr.append((food_times[i],i+1))
    
    arr.sort()
    
    pretime = 0
    for i, letter in enumerate(arr):
        diff = letter[0]- pretime
        
        if diff != 0:
            spend = (diff * n)
            
            if k >= spend:      
                k -= spend
                pretime = letter[0]
            else:
                k %= n
                sublist = sorted(arr[i:], key = itemgetter(1))
                return sublist[k][1]
        n -= 1
        
    return -1   

print(solutuion([3,5,1,6,5,3],20))