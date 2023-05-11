n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 == n2 == n3 == 60:
    print("Equilateral")

elif n1 + n2 + n3 == 180:
    if n1 == n2 or n1 == n3 or n2 == n3:
        print("Isosceles")
    elif n1 != n2 != n3:
        print("Scalene")

elif n1 + n2 + n3 != 180:
    print("Error")
        