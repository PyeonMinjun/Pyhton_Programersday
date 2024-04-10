flag = True

while flag:
    stk = []
    ns = input()
    res = 0
    if ns == ".":
        flag = False
    
    for i in ns:
        if i == "(" or i == "[": 
            stk.append(i)
            
        elif i == ")":
            if stk:
                if stk[-1] == "(":
                    stk.pop()
                else:
                    res = 1
            else:
                res = 1
        
        elif i == "]":
            if stk:
                if stk[-1] == "[":
                    stk.pop()
                else:
                    res = 1
            else:
                res = 1
            
    if flag == False:
        continue

    if stk or res == 1:
        print("no")
    else:
        print("yes")

