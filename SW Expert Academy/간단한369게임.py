n = int(input())
res = []

for i in range(1,n+1):
    i = str(i)
    clap = i.count("3") + i.count("6")+i.count("9")
    
    if not clap:
        print(i, end =" ")
    else:
        print("-" * clap, end = " ")