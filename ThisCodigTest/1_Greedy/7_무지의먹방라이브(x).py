from operator import itemgetter
def solution(food_times, k):
    
    arr = []
    n = len(food_times)
    for i in range(n):
        arr.append(( food_times[i], i+1 ))
    
    arr.sort()
        
    h = 0
    for i,food in enumerate(arr):
        diff = food[0] - h
        if diff != 0:
            spend = diff * n
            if spend <= k:
                k -= spend
                h = food[0]
            else:
                k %= n
                sublist = sorted(food[i:], key= itemgetter(1))
                return sublist[k][1]
                
        n -= 1        
    
    return -1
    
    




