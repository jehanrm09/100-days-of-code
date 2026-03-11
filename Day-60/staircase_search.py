matrix = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
]
target = 29

row = 0
col = len(matrix[0]) - 1

found = False

while row < len(matrix) and col >= 0:
    current = matrix[row][col]
    
    if current == target:
        found = True
        break
    elif current > target:
        col -= 1
    else:
        row += 1

if found:
    print(f"Target {target} found at index: [{row}][{col}]")
else:
    print(f"Target {target} not in matrix.")