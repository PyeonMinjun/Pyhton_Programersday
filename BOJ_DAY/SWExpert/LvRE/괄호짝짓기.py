for tc in range(1,11):
    n = int(input())
    ns = list(map(str,input()))
    stk = []
    flag = 1
    for par in ns:

        if par == "(" or par == "{" or par == "[" or par == "<":
            stk.append(par)
        
        else:
            if par == ")":
                if stk:
                    if stk[-1] == "(":
                        stk.pop()
                    else:
                        flag = 0
                else:
                    flag= 0

            elif par == "}":
                if not stk:
                    flag = 0
                elif stk[-1] == "{":
                    stk.pop()
                else:
                    flag = 0
        
            elif par == ">":
                if not stk:
                    flag = 0 
                elif stk[-1] == "<":
                    stk.pop()
                else:
                    flag= 0
            elif par == "]":
                if not stk:
                    flag = 0

                elif stk[-1] == "[":
                    stk.pop()

                else:
                    flag = 0



    
    if stk or flag == 0:
        print("#{} 0" .format(tc))
    else:
        print("#{} 1" .format(tc))

        
                
        
