n = int(input())

line = 0
end = 0 # 인덱스 끝값
while n > end:
    line += 1
    end += line
    
    
diff = end - n

if line % 2 == 0:
    top = line - diff
    bot = diff + 1
    
else:
    top = diff + 1
    bot = line - diff


print("{}/{}" .format(top,bot))