pangram = input()


for i in range(26):
    o = chr(i+65)
    ou = chr(i+97)

    if pangram.find(o) == -1:
        if pangram.find(ou) == -1 :
            print("NO")
            break
            
else:
    print("YES")