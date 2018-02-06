from Cube import *
from Cylinder import *
from Mesh import *
from Renderer import *


def main():
    randy = Renderer()

    polyCube = Cube()
    polyCube.build_polygon_mesh()
    randy.render(polyCube.mesh, 512, "polyCube.jpg")

    triangleCube = Cube()
    triangleCube.build_triangle_mesh(4000)
    randy.render(triangleCube.mesh, 1080, "HDcube.jpg")

    polyCylinder = Cylinder()
    polyCylinder.build_polygon_mesh()
    randy.render(polyCylinder.mesh, 512, "polyCylinder.jpg")

    triangleCylinder = Cylinder()
    triangleCylinder.build_triangle_mesh(4000)
    randy.render(triangleCylinder.mesh, 1080, "HDcylinder.jpg")


if __name__ == "__main__":
    main()
