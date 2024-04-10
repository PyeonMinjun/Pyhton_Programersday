while True:
    n = int(input())
    arr = []
    for i in range(1,n+1):
        if n % i == 0:
            arr.append(i)

    if n == -1:
        break
    
    if n == sum(arr[:len(arr) - 1]):
        print("{} =" .format(n) , end="")
        for i in arr[:len(arr)-2]:
            print(" {} +" .format(i), end="")
        
        print(" {}". format(arr[len(arr)-2]))
    else:
        print("{} is NOT perfect." .format(n))
            
            
