arr = [0] * 10
n = input()


for i in n:
    if i == '9' or i == '6':
        if arr[9] <= arr[6]:
            arr[9] += 1
        else:
            arr[6] += 1
    else:
        arr[int(i)] += 1
print(max(arr))