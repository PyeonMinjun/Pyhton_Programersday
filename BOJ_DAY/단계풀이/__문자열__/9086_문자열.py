n = int(input())
for _ in range(n):
    xs = input()
    xss = xs[0] + xs[-1]
    # xss = [xs[i] for i in (0,-1)]
    # xss = xs[::len(xs)-1]
    print(xss)