def solution(mylist):
    x = []
    for i in mylist:
        x.append(len(i))    
    return x


print(solution([[1], [2]]))