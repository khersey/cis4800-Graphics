from Cube import *
from Cylinder import *
from Sphere import *
from Mesh import *
from Face import *
import mathUtil


def test():
    # set up tests
    cubeFactory = Cube()
    sphereFactory = Sphere()
    cylinderFactory = Cylinder()

    cube = cubeFactory.build_triangle_mesh(256)
    sphere = sphereFactory.build_triangle_mesh(256)
    cylinder = cylinderFactory.build_triangle_mesh(256)

    # do tests
    print("#### CUBE ####")
    cube.test_integrity()
    print("\n")

    print("#### CYLINDER ####")
    cylinder.test_integrity()
    print("\n")

    print("#### SPHERE ####")
    sphere.test_integrity()
    print("\n")


if __name__ == "__main__":
    test()