def solution(s):
    answer = len(s)
    n = len(s)
    
    
    for step in range(1, n//2 + 1):
        k = s[0:step]    
        compress = ''
        cnt = 1
        
        for j in range(step,n,step):
            if k == s[j:j+step]:
                cnt += 1
            
            else:
                compress += str(cnt) + k if cnt >= 2 else k
                k = s[j:j+step]
                cnt = 1
            
        compress += str(cnt) + k if cnt >= 2 else k
        answer = min(answer,len(compress))
    
    return answer

print(solution('aabbaccc'))