text = input()
flag = False

Lip = []
for i in range(26):
    a = chr(i+65)
    b = chr(i+97)
    
    if text.find(a) == -1:
        if text.find(b) == -1:
            Lip.append(b)
            flag = True
            
    
if flag:
    print("YES")
    print("".join(Lip))
    
else:
    print("NO")