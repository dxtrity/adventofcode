def find_xmas(grid):
    directions = [(row_step, col_step) for row_step in [-1, 0, 1] for col_step in [-1, 0, 1] if (row_step, col_step) != (0, 0)]
    rows, cols = len(grid), len(grid[0])
    xmas_count = 0
    
    for row in range(rows):
        for col in range(cols):
            for row_step, col_step in directions:
                found = all(
                    0 <= row + i * row_step < rows and 
                    0 <= col + i * col_step < cols and 
                    grid[row + i * row_step][col + i * col_step] == 'XMAS'[i]
                    for i in range(4)
                )
                xmas_count += found
    
    return xmas_count

with open("data", 'r') as file:
    grid = [list(line.strip()) for line in file]

if grid:
    print(find_xmas(grid))