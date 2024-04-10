val = int(input())
#큰 단위 화폐부터 차례대로 확인
arr = [500,100,50,10]
res = 0

for i in arr:
    res += val // i # 해당 화폐로 거슬러 줄 수 있는 동저느이 개수 세기
    val %= i

print(res)
