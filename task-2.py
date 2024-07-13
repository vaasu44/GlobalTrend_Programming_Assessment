"""2.	Write a Python function that takes a 2D list (matrix) and returns its transpose."""

def transpose(matrix):
    # Initialize an empty list to hold the transposed matrix
    transposed_matrix = []

    # Iterate over the columns of the original matrix
    for i in range(len(matrix[0])):
        # Create a new row for the transposed matrix
        new_row = []
        for j in range(len(matrix)):
            # Append the element from the original matrix to the new row
            new_row.append(matrix[j][i])
        # Append the new row to the transposed matrix
        transposed_matrix.append(new_row)
    
    return transposed_matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose the matrix
transposed = transpose(matrix)

# Print the transposed matrix
print("transposed matrix is: ")
for row in transposed:
    print(row)
