from operator import itemgetter
n = int(input())
card_dict = {}

for i in range(n):
    card = int(input())
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

# 방법 1 itemgtter 사용
# result = sorted(card_dict.items(), key=itemgetter(0))
# result.sort(key=itemgetter(1),reverse=True)
# print(result[0][0])

# 방법 2 람다식 사용
result = sorted(card_dict.items(), key= lambda x:(-x[1],x[0]))
# print(result)
print(result[0][0])