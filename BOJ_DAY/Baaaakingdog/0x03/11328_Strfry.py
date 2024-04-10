n = int(input())




for i in range(n):
    arr1 = [0] * 26
    arr2 = [0] * 26 
    ns1 = []
    ns2 = []
    a,b = input().split()

    ns1 = list("".join(a))    
    ns2 = list("".join(b))
    

    for i in ns1:
        arr1[ord(i)-97] += 1
    for i in ns2:
        arr2[ord(i)-97] += 1
    
   
    if arr1 == arr2:
        print("Possible")
    else:
        print("Impossible")