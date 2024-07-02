def count_adjacent_mines(grid):
    num_of_rows = len(grid)
    num_of_columns = len(grid[0])

    def valid_indices(row, col):
        return 0 <= row < num_of_rows and 0 <= col < num_of_columns

    for row_num in range(num_of_rows):
        for col_num in range(num_of_columns):
            if grid[row_num][col_num] == '-':
                counter = 0
                for i in range(-1, 4):
                    for j in range(-2, 1):
                        if valid_indices(row_num + i, col_num + j) and grid[row_num + i][col_num + j] == '#':
                            counter += 1
                grid[row_num][col_num] = str(counter)
    
    return grid

# Test the function with an example grid
possible_grid = [
    ['#', '-', '-', '#'],
    ['-', '#', '-', '-'],
    ['#', '-', '-', '-']
]

print("original grid:")
for row in possible_grid:
    print(row)

modified_grid = count_adjacent_mines(possible_grid)

print("\nModified Grid:")
for row in modified_grid:
    print(row)