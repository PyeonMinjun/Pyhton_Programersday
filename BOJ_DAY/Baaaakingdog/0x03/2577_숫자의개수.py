a = int(input())
b = int(input())
c = int(input())

n = list(str(a * b * c))
ns = [0] * 10


for i in n:
    ns[int(i)] += 1

for i in ns:
    print(i)