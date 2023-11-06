# 닫는 괄호가 나오면
 # 그 전 괄호가 여는 괄호이면
 # 결과에 저장
# pop
# // 

n = list(input())
stk = []
res = 1
sum = 0

for i in range(len(n)):
    if n[i] == '(':
        stk.append('(')
        res *= 2
        
    elif n[i] == '[':
        stk.append('[')
        res *= 3
        
    elif n[i] == ')':
        if stk and stk[-1] == "(":
            if n[i-1] == "(":
                sum += res
            stk.pop()
            res = res // 2
        else:
            print(0)
            exit(0)
        
    elif n[i] == ']':
        if stk and stk[-1] == "[":
            if n[i-1] == "[":
                sum += res
            stk.pop()
            res = res // 3
        else:
            print(0)
            exit(0)
        
if stk:
    print(0)
    exit(0)
else:
    print(sum)
        

        
        
        

 