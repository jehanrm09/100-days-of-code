matrix = [
    [10, 20],
    [30, 40],
    [50, 60]
]

rows = len(matrix)
cols = len(matrix[0])

transposed = []
for i in range(cols):
    new_row = [0] * rows
    transposed.append(new_row)

for r in range(rows):
    for c in range(cols):

        transposed[c][r] = matrix[r][c]

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed:
    print(row)