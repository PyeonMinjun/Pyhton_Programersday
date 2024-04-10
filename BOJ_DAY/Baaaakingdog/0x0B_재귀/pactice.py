# 재귀로 N부터 1까지 출력하는 함수
# 1부터 N까지의 합을 구하는 함수를 한 번 짜보는 시간을 가져보자.



def func1(n):
    if n == 1:
        return 1
    print(n)
    return func1(n-1)

# print(func1(10))

def func2(n):
    if n == 1:
        return 1
    
    return func2(n-1) +  n 

print(func2(10))