from math import *

def x_rotation(angle):
    return [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, cos(angle), -sin(angle), 0.0],
        [0.0, sin(angle), cos(angle), 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ]

def z_rotation(angle):
    return [
        [cos(angle), -sin(angle), 0.0, 0.0],
        [sin(angle), cos(angle), 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ]

def y_rotation(angle):
    # NOTE: THIS DOES NOT WORK YET, it's copy pasta of z_rotation
    return [
        [cos(angle), -sin(angle), 0.0, 0.0],
        [sin(angle), cos(angle), 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
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
    