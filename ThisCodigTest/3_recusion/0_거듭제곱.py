# 연습문제 1 - 거듭제곱

# a^b mod m  구하기.


def func1(a,b,m):
    val = 1
    while b:
        b -= 1
        val *= a
    return (val % m)

print(func1(6,100,5))

# 해결해주려면 곱하는 중간 중간 계속 m으로 나눠서 나머지만 챙기자.
## c++ 에서 int 범위를 넘어서서 longlong으로 바꿔야하지만
def func2(a,b,m):
    val = 1
    while b:
        b -= 1
        val = (val * a) % m
    return val

print(func2(6,100,5))
