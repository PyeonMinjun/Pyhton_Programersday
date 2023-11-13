
n = int(input())

arr = []

for i in range(1, n+1):
    ns = str(i)
    
    clap = ns.count('3') + ns.count("6") + ns.count("9")
    
    if clap == 0:
        print(i, end=" ")
    else:
        print("-" * clap, end=' ')

            
        
        
    