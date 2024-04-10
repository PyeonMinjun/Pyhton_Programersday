# 1. 표1을 보고 입력받은 문자들을 각각 대응하는 숫자로 변경한다.
# 2. 각 숫자들을 6자리 이진수로 표현하고, 이 이진수들을 한 줄로 쭉 이어 붙인다.
# 3. 한 줄로 쭉 이어붙인 이진수들을 8자리씩 끊어서 십진수로 바꾼다.
# 4. 각각의 십진수를 아스키 코드로 변환한다.

n = int(input())
arr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

for tc in range(1,n+1):
    ms = input()
    val = []
    for i in range(len(ms)):
        val.append(arr.index(ms[i]))
    bin_val = ''
    
    for i in val:
        binv = (bin(i)[2:])
        while len(binv) < 6:
            binv = "0" + binv
             
        bin_val += binv
    
    r = ''
    for w in range(len(ms)*6 // 8):
        
        e = int(bin_val[w* 8:w*8+8],2)
        r += chr(e)
    print("#{} {}" . format(tc, r))