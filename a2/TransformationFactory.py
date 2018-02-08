from math import *

def x_rotation(angle):
    # turns out sin and cos expect radians
    r = radians(angle)

    return [
        [1.0, 0.0,    0.0,     0.0],
        [0.0, cos(r), -sin(r), 0.0],
        [0.0, sin(r), cos(r),  0.0],
        [0.0, 0.0,    0.0,     1.0]
    ]

def z_rotation(angle):
    # turns out sin and cos expect radians
    r = radians(angle)

    return [
        [cos(r), -sin(r), 0.0, 0.0],
        [sin(r), cos(r),  0.0, 0.0],
        [0.0,    0.0,     1.0, 0.0],
        [0.0,    0.0,     0.0, 1.0]
    ]

def y_rotation(angle):
    # turns out sin and cos expect radians
    r = radians(angle)

    return [
        [cos(r), 0.0, -sin(r), 0.0],
        [0.0,    1.0, 0.0,     0.0],
        [sin(r), 0.0, cos(r),  0.0],
        [0.0,    0.0, 0.0,     1.0]
    ]

def translation(x,y,z):
    return [
        [1.0, 0.0, 0.0, x],
        [0.0, 1.0, 0.0, y],
        [0.0, 0.0, 1.0, z],
        [0.0, 0.0, 0.0, 1.0]
    ]

def scale(x, y, z):
    return [
        [x,   0.0, 0.0, 0.0],
        [0.0, y,   0.0, 0.0],
        [0.0, 0.0, z,   0.0],
        [0.0, 0.0, 0.0, 1.0]
    ]

def view_plane_projection(x):
    return [
        [x,   0.0, 0.0, 0.0],
        [0.0, x,   0.0, 0.0],
        [0.0, 0.0, x,   0.0],
        [0.0, 0.0, 1.0, 0.0]
    ]

def augmented_basis_change(U,V,N,C)
    return [
            [U[0], V[0], N[0], 1.0, 0.0, 0.0, C[0]],
            [U[1], V[1], N[1], 0.0, 1.0, 0.0, C[1]],
            [U[2], V[2], N[2], 0.0, 0.0, 1.0, C[2]]
        ]