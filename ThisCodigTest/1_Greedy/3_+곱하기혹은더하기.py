data = input()

#첫번째 문자를 숫자로 변환
res = int(data[0])


for i in range(1,len(data)):
    num = int(data[i])   
    # 두수 중 하나라도 '0'혹은 '1'인 경우, 곱하기보다는 더하기 수행  
    if res <= 1 or num <= 1:
        res += num
        
    else:
        res *= num

print(res)