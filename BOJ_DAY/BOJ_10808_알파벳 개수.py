text = input()
res = [0] * 26


for k in text:
    for i in range(97,123): # 1 ~ 28
        if k == chr(i):
            res[i-97] += 1

print(" ".join(map(str, res)))