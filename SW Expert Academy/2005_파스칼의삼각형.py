n = int(input())

for i in range(1,n+1):
    total = 0
    st = int(input())

    arr = [ [0] * st  for _ in range(st)]
    
    arr[0][0] = 1    
    for row in range(1,st):
        arr[row][0] = 1
        for col in range(1,st):
            arr[row][col] = arr[row-1][col-1] + arr[row-1][col]
  
    print("#{} ".format(i))
    
    for i in range(st):
        for j in range(i+1):
            print(arr[i][j], end= "")
        print()


    # for ar in arr:
    #     print()
    #     for a in ar:
    #         if a:
    #             print(a, end = " ")
    # print()

  
# print(arr)

