import random
import math

from Face import *

# returns a 3-tuple
def cross_product(v1, v2):
    # x=0, y=1, z=2
    return (
        v1[1]*v2[2] - v2[1]*v1[2], # x = y1z2 - y2z1
        v1[0]*v2[2] - v2[0]*v1[2], # y = x1z2 - x2z1
        v1[0]*v2[1] - v2[0]*v1[1]  # z = x1y2 - x2y1
    )

def vector_from_points(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])

# return a float
def dot_product(v1, v2):
    return float(v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2])

# apply 4x4 matrix transformation to a set of coordinates
def apply_transformation(coordinates, matrix):
    new_coordinates = [0.0, 0.0, 0.0, 0.0]

    original = list(coordinates)
    original.append(1)

    for i in range(0,4):
        for j in range(0,4):
            new_coordinates[i] += original[j] * matrix[i][j]

    if new_coordinates[3] == 0.0:
        print("Error: z-val is 0 after transform")
        return (new_coordinates[0], new_coordinates[1], -1)

    if new_coordinates[3] != 1.0:
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
            #matrix[i][k] = 0.0

    # backfill or something
    for k in range(m-1, 0-1, -1):
        divider = matrix[k][k]
        for i in range(0, k):
            for j in range(n-1, k-1, -1):
                matrix[i][j] -= matrix[k][j] * matrix[i][k] / divider
        matrix[k][k] /= divider

        for i in range(m, n):
            matrix[k][i] = matrix[k][i] / divider
            if abs(matrix[k][i]) < 0.0000000001:
                matrix[k][i] = 0.0

    return True

def random_color():
    random.seed(None)
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    return (r,g,b)

def to_unit_vector(vector):
    magnitude = math.sqrt(vector[0]*vector[0] + vector[1]*vector[1] + vector[2]*vector[2])
    if magnitude == 0.0:
        return (0,0,0)
    x = vector[0] / magnitude
    y = vector[1] / magnitude
    z = vector[2] / magnitude
    return (x,y,z)

def transform_faces(face_list, transformation):
    solution_dict = {}

    for index in range(0, len(face_list)):
        face = face_list[index]

        v1 = face.v1
        new_v1 = solution_dict.get(v1)
        if new_v1 == None:
            new_v1 = apply_transformation(v1, transformation)
            solution_dict[v1] = new_v1
        face.v1 = new_v1

        v2 = face.v2
        new_v2 = solution_dict.get(v2)
        if new_v2 == None:
            new_v2 = apply_transformation(v2, transformation)
            solution_dict[v2] = new_v2
        face.v2 = new_v2
        
        v3 = face.v3
        new_v3 = solution_dict.get(v3)
        if new_v3 == None:
            new_v3 = apply_transformation(v3, transformation)
            solution_dict[v3] = new_v3
        face.v3 = new_v3

        face.generate_normal()
        
        face_list[index] = face

    return face_list

def transform_edges(edge_list, transformation):
    solution_dict = {}

    for index in range(0, len(edge_list)):
        edge = edge_list[index]

        v1 = edge[0]
        new_v1 = solution_dict.get(v1)
        if new_v1 == None:
            new_v1 = apply_transformation(v1, transformation)
            solution_dict[v1] = new_v1

        v2 = edge[1]
        new_v2 = solution_dict.get(v2)
        if new_v2 == None:
            new_v2 = apply_transformation(v2, transformation)
            solution_dict[v2] = new_v2

        edge_list[index] = (new_v1, new_v2)
    
    return edge_list

