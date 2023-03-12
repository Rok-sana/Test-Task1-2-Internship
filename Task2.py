vectors = [(-1,0), (1, 0), (0, -1), (0, 1)]

def numIslands(grid):
    count = 0
    data = grid
    for i, row_value in enumerate(grid):
        for j, column_value in enumerate(row_value):
            if dfs(data, i, j) > 0:
                count += 1
    return count

def dfs(data, row, column):
    if not isValid(data, row, column):
        return 0
    data[row][column] = 0
    count = 1
    for vector in vectors:
        i = row + vector[0]
        j = column + vector[1]
        count += dfs(data, i, j)
    return count

def isValid(data, row, column):
    rows = len(data)
    columns = len(data[0])
    return (row < rows and row >= 0) and (column < columns and column >= 0) and (data[row][column] == 1)