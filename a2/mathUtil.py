
# returns a 3-tuple
def cross_product(v1, v2):
    # x=0, y=1, z=2
    return (
        v1[1]*v2[2] - v2[1]*v1[2], # x = y1z2 - y2z1
        v1[0]*v2[2] - v2[0]*v1[2], # y = x1z2 - x2z1
        v1[0]*v2[1] - v2[0]*v1[1]  # z = x1y2 - x2y1
    )

# apply 4x4 matrix transformation to a set of coordinates
def apply_transformation(coordinates, matrix):
    new_coordinates = [0.0, 0.0, 0.0, 0.0]

    original = list(coordinates)
    original.append(1)

    for i in range(0,4):
        for j in range(0,4):
            new_coordinates[i] += original[j] * matrix[i][j]

    if new_coordinates[3] != 1:
        for i in range(0,3):
            if new_coordinates[i] != 0.0:
                new_coordinates[i] /= new_coordinates[3]
            
    return tuple(new_coordinates[:3])

# add matrix multiplication
def matrix_multiplication(matrix1, matrix2):
    out_matrix = [[0 for i in range(4)] for k in range(4)]
    for row in range(0,4):
        for col in range(0,4):
            for index in range(0,4):
                out_matrix[row][col] += matrix1[row][index] * matrix2[index][col]

    return out_matrix

# based on wikipedia algorithm
def gaussian_elimination(matrix):
    m, n = len(matrix), len(matrix[0])

    for k in range(0, min(m,n)):
        i_max = k
        for i in range(k, m):
            if abs(matrix[i][k]) > abs(matrix[i_max][k]):
                i_max = i
        if matrix[i_max][k] == 0:
            return False
        matrix[k], matrix[i_max] = matrix[i_max], matrix[k]

        for i in range(k+1, m):
            f = matrix[i][k] / matrix[k][k]
            for j in range(k+1, n):
                matrix[i][j] -= matrix[k][j] * f
            matrix[i][k] = 0.0

    # backfill or something
    for k in range(m-1, 0-1, -1):
        divider = matrix[k][k]
        for i in range(0, k):
            for j in range(n-1, k-1, -1):
                matrix[i][j] -= matrix[k][j] * matrix[i][k] / divider
        matrix[k][k] /= divider

        for i in range(m, n):
            matrix[k][i] = round(matrix[k][i] / divider)

    return True

