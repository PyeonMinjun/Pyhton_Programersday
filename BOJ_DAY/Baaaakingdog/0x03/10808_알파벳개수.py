s = input()

arr = [0] * 26

for i in s:
    o = ord(i) - 97
    arr[o] += 1

print(" ".join(map(str,arr)))