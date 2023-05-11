a,b,c = map(int,input().split())

val = max(a,b,c)
rest = (a+ b+ c) - val


if ( a+b+c )- val <= val:
   val = ((a+b+c) - val -1)
    
print(rest + val)