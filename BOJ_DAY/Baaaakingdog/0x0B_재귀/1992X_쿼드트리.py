def solve(n, y, x):
    if n == 1:
        print(arr[y][x], end='')
        return

    zero = True
    one = True

    for i in range(y, y + n):
        for j in range(x, x + n):
            if arr[i][j] == 1:
                zero = False
            else:
                one = False

    if zero:
        print(0, end='')
    elif one:
        print(1, end='')
    else:
        print("(", end='')
        solve(n // 2, y, x)  # 왼쪽 위
        solve(n // 2, y, x + n // 2)  # 오른쪽 위
        solve(n // 2, y + n // 2, x)  # 왼쪽 아래
        solve(n // 2, y + n // 2, x + n // 2)  # 오른쪽 아래
        print(")", end='')

        
                



n = int(input())
arr=  [list(map(int,input())) for _ in range(n)]
solve(n,0,0)


