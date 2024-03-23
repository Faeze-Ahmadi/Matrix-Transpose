def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


# Take matrix input from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
print("Enter matrix elements:")
for i in range(rows):
    # Read a line of input, split it into numbers, and convert them to integers
    row_input = input().split()
    row = [int(num) for num in row_input]
    matrix.append(row)

# Display the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Transpose the matrix and display the result
transposed_matrix = transpose_matrix(matrix)
print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)

