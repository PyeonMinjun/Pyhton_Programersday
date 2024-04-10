t = int(input())

for tc in range(1,t+1):
    ns = list(map(int,input().split()))
    if ns[0] > ns[1]:
        print("#{} >" .format(tc))
    elif ns[0] < ns[1]:
        print("#{} <" .format(tc))
    else:
        print("#{} =" .format(tc))
        