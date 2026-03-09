matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)
primary_sum = 0
secondary_sum = 0

for i in range(n):
    primary_sum += matrix[i][i]
    
    secondary_sum += matrix[i][n - 1 - i]

print("Matrix Grid:")
for row in matrix:
    print(row)

print("-" * 15)
print(f"Primary Diagonal Sum: {primary_sum}")
print(f"Secondary Diagonal Sum: {secondary_sum}")