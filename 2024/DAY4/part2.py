count = 0

data = open("data").read().strip()

grid = data.split('\n')
rows = len(grid)
cols = len(grid[0])

for row in range(rows):
    for col in range(cols):
        if row+2<rows and col+2<cols and grid[row][col]=='M' and grid[row+1][col+1]=='A' and grid[row+2][col+2]=='S' and grid[row+2][col]=='M' and grid[row][col+2]=='S':
            count += 1
        if row+2<rows and col+2<cols and grid[row][col]=='M' and grid[row+1][col+1]=='A' and grid[row+2][col+2]=='S' and grid[row+2][col]=='S' and grid[row][col+2]=='M':
            count += 1
        if row+2<rows and col+2<cols and grid[row][col]=='S' and grid[row+1][col+1]=='A' and grid[row+2][col+2]=='M' and grid[row+2][col]=='M' and grid[row][col+2]=='S':
            count += 1
        if row+2<rows and col+2<cols and grid[row][col]=='S' and grid[row+1][col+1]=='A' and grid[row+2][col+2]=='M' and grid[row+2][col]=='S' and grid[row][col+2]=='M':
            count += 1

# fuck this question
print(count)