import * from math

# returns a 3-tuple
def cross_product(v1, v2):
    # x=0, y=1, z=2
    return (
        v1[1]*v2[2] - v2[1]*v1[2], # x = y1z2 - y2z1
        v1[0]*v2[2] - v2[0]*v1[2], # y = x1z2 - x2z1
        v1[0]*v2[1] - v2[0]*v1[1]  # z = x1y2 - x2y1
    )

