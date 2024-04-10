def solve(n, y, x):
    if n == 1:
        print(arr[y][x], end='')
        return

    zero = all(arr[i][j] == 0 for i in range(y, y + n) for j in range(x, x + n))
    one = all(arr[i][j] == 1 for i in range(y, y + n) for j in range(x, x + n))

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


if __name__ == "__main__":
    N = int(input())
    MAX = 64
    arr = [[0] * MAX for _ in range(MAX)]

    for i in range(N):
        str_input = input().strip()
        for j in range(N):
            arr[i][j] = int(str_input[j])

    solve(N, 0, 0)
