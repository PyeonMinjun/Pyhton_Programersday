def func1(a,b,m):
    val = 1
    while b:
        b -= 1
        val *= a
    return val % m



print(func1(6,100,5))

def func2(a,b,m):
    val = 1
    while b:
        b -= 1
        val = (val * a) % m
    return val

print(func2(6,100,5))
