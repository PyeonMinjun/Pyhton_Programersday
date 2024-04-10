# a의 b제곱을 m으로 나눈 나머지를 재귀로 풀어라.


#1.a를 b번 곱한다.
def func1(a,b,m):
    val = 1
    while b:
        b -= 1
        val *= a
    return val % m
    
# int over flow를 고려한 방식
def func1_1(a,b,m):
    val = 1
    while (b):
        b -= 1 
        val = val * a % m
        return val

print(func1(6,100,5))
print(func1_1(6,100,5))