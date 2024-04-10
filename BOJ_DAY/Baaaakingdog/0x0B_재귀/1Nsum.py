# 재귀로 N부터 1까지 출력하는 함수

def nsum(x):
    if x == 0:
        return
    print(x, end = " ")
    nsum(x-1)

nsum(3)

# 1부터 N까지의 합을 구하는 함수
def func2(n):
    if n <= 1:
        return n
    return n+ func2(n-1)    
print()
print(func2(0))
        
    