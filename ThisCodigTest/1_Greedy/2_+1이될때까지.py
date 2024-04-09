n,t = map(int,input().split())

res = 0


while True:
    # N이 t로 나누어 떨어지는 수가 될때까지 빼기
    total = (n // t) * t
    res += n - total 
    n = total  
    
    # N이 t보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < t :
        break
    # t로 나누기
    res += 1
    n = n // t

#마지막으로 남은 수에 대하여 1씩 빼기.
res += n-1
print(res)



