# from itertools import zip_longest

# arr = []
# arr2 = []

# for _ in range(5):
#     n = input()
#     arr.append(n)

# arr1 = list(zip_longest(*arr, fillvalue=''))

# for i in arr1: 
#     for j in i:
#         arr2.append(j)

# print("".join(arr2))



#=========================================#

words = []
length = []

for i in range(5):
    word = input()
    words.append(word)
    length.append(len(word))


rst = ""
for i in range(max(length)): # 5
    for j in range(5): # 5
        if i < length[j]:
            rst += words[j][i]
            
print(rst)
