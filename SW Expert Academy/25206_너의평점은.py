sum = 0
sum_pass = 0
major_sum = 0
for i in range(20):
    major, score, PF = input().split()
    
    
    if PF == "P":
        continue
    else:
        major_sum += float(score)
        
        if PF == "F":
            continue
        
        elif PF == "A+":
            sum += (float(score) * 4.5)
        
        elif PF == "A0":
            sum += (float(score) * 4.0)
            
        elif PF == "B+":
            sum += (float(score) * 3.5)
            
        elif PF == "B0":
            sum += (float(score) * 3.0)
            
        elif PF == "C+":
            sum += (float(score) * 2.5)
            
        elif PF == "C0":
            sum += (float(score) * 2.0)
            
        elif PF == "D+":
            sum += (float(score) * 1.5)
        
        elif PF == "D0":
            sum += (float(score) * 1.0)
        
        elif PF == "P":
            continue
    
print(sum / (major_sum))
        

    
