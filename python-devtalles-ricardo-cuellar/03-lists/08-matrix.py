matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

print(matrix) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1]) # [4, 5, 6]
print(matrix[1][1]) # 5

# update a matrix address
matrix[1][1] = 10
print(matrix) # [[1, 2, 3], [4, 10, 6], [7, 8, 9]]
