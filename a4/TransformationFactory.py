from math import *
import mathUtil

# angle in degrees
def x_rotation(angle):
    # turns out sin and cos expect radians
    r = radians(angle)

    return [
        [1.0, 0.0,    0.0,     0.0],
        [0.0, cos(r), -sin(r), 0.0],
        [0.0, sin(r), cos(r),  0.0],
        [0.0, 0.0,    0.0,     1.0]
    ]

# angle in degrees
def z_rotation(angle):
    # turns out sin and cos expect radians
    r = radians(angle)

    return [
        [cos(r), -sin(r), 0.0, 0.0],
        [sin(r), cos(r),  0.0, 0.0],
        [0.0,    0.0,     1.0, 0.0],
        [0.0,    0.0,     0.0, 1.0]
    ]

# angle in degrees
def y_rotation(angle):
    # turns out sin and cos expect radians
    r = radians(angle)

    return [
        [cos(r), 0.0, -sin(r), 0.0],
        [0.0,    1.0, 0.0,     0.0],
        [sin(r), 0.0, cos(r),  0.0],
        [0.0,    0.0, 0.0,     1.0]
    ]

# reposition the object
def translation(x,y,z):
    return [
        [1.0, 0.0, 0.0, x],
        [0.0, 1.0, 0.0, y],
        [0.0, 0.0, 1.0, z],
        [0.0, 0.0, 0.0, 1.0]
    ]

# x, y, z are scaling factors
def scale(x, y, z):
    return [
        [x,   0.0, 0.0, 0.0],
        [0.0, y,   0.0, 0.0],
        [0.0, 0.0, z,   0.0],
        [0.0, 0.0, 0.0, 1.0]
    ]

# d = distance to view plane
def to_screen_space(d, h, f):
    return [
        [d/h, 0.0, 0.0,      0.0],
        [0.0, d/h, 0.0,      0.0],
        [0.0, 0.0, f/(f-d), -((f*d)/(f-d))],
        [0.0, 0.0, 1.0,      0.0]
    ]

# frame(C, basis(U,V,N))
def basis_change(U,V,N,C):
    augmented_identity_mtx = [
        [U[0], V[0], N[0], 1.0, 0.0, 0.0, -C[0]],
        [U[1], V[1], N[1], 0.0, 1.0, 0.0, -C[1]],
        [U[2], V[2], N[2], 0.0, 0.0, 1.0, -C[2]]
    ]
    print("before basis change:")
    print(augmented_identity_mtx)
    mathUtil.gaussian_elimination(augmented_identity_mtx)
    print("after basis change:")
    print(augmented_identity_mtx)
    return [
        augmented_identity_mtx[0][3:],
        augmented_identity_mtx[1][3:],
        augmented_identity_mtx[2][3:],
        [0, 0, 0, 1]
    ]
     
# m by m = image area 
def to_canvas(m):
    return [
        [0.0,    -m/(2.0),  0.0, (m/2.0)-0.5],
        [m/(2.0), 0.0,      0.0, (m/2.0)-0.5],
        [0.0,     0.0,      1.0, 0.0],
        [0.0,     0.0,      0.0, 1.0]
    ]