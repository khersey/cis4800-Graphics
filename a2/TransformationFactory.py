from math import *

def x_rotation(angle):
    # turns out sin and cos expect radians
    r = radians(angle)
    
    return [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, cos(r), -sin(r), 0.0],
        [0.0, sin(r), cos(r), 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ]

def z_rotation(angle):
    # turns out sin and cos expect radians
    r = radians(angle)

    return [
        [cos(r), -sin(r), 0.0, 0.0],
        [sin(r), cos(r), 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ]

def y_rotation(angle):
    # turns out sin and cos expect radians
    r = radians(angle)

    return [
        [cos(r), 0.0, -sin(r), 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [sin(r), 0.0, cos(r), 0.0],
        [0.0, 0.0, 0.0, 1.0]
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
