
def gcd(a ,b ):
    x,y = a, b 
    while x:
        x,y = y%x, x  # 나눈 나머지를 나누는 값으로 설정 / 그전에있던 나누는값은 몫 
    return y                # 나머지가 0이되면  종료후 나눴던 값 출력
        