def fill_centered_triangle(grid_size):
    # Create a grid filled with zeros
    grid = [[0] * grid_size for _ in range(grid_size)]

    # Calculate the starting point for each row to center the top vertex
    start_col = (grid_size - 1) // 2

    # Fill the bottom row with 1s
    grid[grid_size - 1] = [1] * grid_size

    # Fill the top row with a single 1 at the center
    grid[0][start_col] = 1

    # Fill the cells in between to form a triangular shape
    for i in range(1, grid_size - 1):
        filled_cells = min(i + 1, grid_size - i)
        # Fill the appropriate cells in each row
        for j in range(start_col - i, start_col + i + 1):
            grid[i][j] = 1

    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))

# Example usage:
grid_size = 5
triangle_grid = fill_centered_triangle(grid_size)
print_grid(triangle_grid)