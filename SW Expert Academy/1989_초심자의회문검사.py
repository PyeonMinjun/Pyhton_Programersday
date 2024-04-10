n = int(input())


for tc in range(1, n+1):
    ns = input()
    rns = ns[::-1]
    if ns == rns:
        print("#{} 1" .format(tc))
    else:
        print("#{} 0" .format(tc))
