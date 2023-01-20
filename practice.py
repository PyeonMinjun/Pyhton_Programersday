k = {
    "R": [ 0,  1],
    "L": [ 0, -1],
    "U": [-1,  0],
    "D": [ 1,  0]
}

m = [
    "#.##",
    "#...",
    "#..."
]

height = 3
width = 4

x = 4
y = 3

code = "LLUU"

for c in code:
    dx = x + k[c][0]
    dy = y + k[c][1]
    
    if 0 <= dx and dx < height and 0 <= dy and dy <= width :
        if m[dx][dy] != "#":
            x = dx
            y = dy
        
print(x+1, y+1)