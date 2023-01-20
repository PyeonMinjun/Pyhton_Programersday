t = int(input())


for _ in range(t):
    n,m,k = map(int,input().split()) 
    a = list(map(int,input().split())) 

    xs = a[k-1:]                         # k부터 배열 선택
    pr_xs = len(a[:k]) - 1               # k 배열의 이전 길이
    cnt = 0                # xs배열부터 1씩증가하며 갯수를 세기위함
    print

    for i in xs:   
        cnt += 1
        if ( a[k-1] + m )  <= i:
            print(pr_xs+ cnt)
            break

    else:
        print("JB")