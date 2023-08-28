def island_perimeter(grid):
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Add 4 sides initially
                
                # Check neighboring cells and subtract sides if adjacent cell is land
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract 2 sides for shared edge
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Subtract 2 sides for shared edge
    
    return perimeter