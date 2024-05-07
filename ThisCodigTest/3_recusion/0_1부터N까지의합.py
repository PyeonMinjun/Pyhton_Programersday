# **재귀로 N부터 1까지 출력하는 함수**

# **1부터 N까지의 합을 구하는 함수**를 한 번 짜보는 시간을 가져보자.
def func1(n):
    if n == 0:
        return 
    print(n, end = " ")
    func1(n-1)


func1(5)