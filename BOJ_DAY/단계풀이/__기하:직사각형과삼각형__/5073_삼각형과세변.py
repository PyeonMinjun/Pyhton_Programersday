while True:
    a,b,c = (map(int,input().split()))
    
    val = max(a,b,c)
    
    if a == 0 and b == 0 and c == 0:
        break
    
    elif (a+b+c) - val  <= val:
        print("Invalid")
    
    elif a == b == c:
        print("Equilateral")
        
    elif a == b or a == c or b == c:
        print("Isosceles")
        
    elif a != b != c:
        print("Scalene")
    