br = True
arr = []

while br:
    ns = input()
    ns = " ".join(ns)
    stk = []
    a = ""
    
    if ns == ".":
        break
    
    for i in ns:
        if i == "(":
            stk.append(i)
        elif i == "[":
            stk.append(i)
            
        elif i == ")":
            if not stk:
                a = "no"
                break
            
            elif stk[-1] == "(":
                stk.pop()

            else:
                a = "no"
                break
            
        elif i == "]":
            if not stk:
                a = "no"
                break
            
            if stk[-1] == "[":
                stk.pop()
            else:
                a = "no"
                break
        
        # elif ns == ".":
        #     br = False
        
    if stk or a == "no":
       print("no")
    else:
        # if br == False:
        #     continue
        print("yes")
        


    