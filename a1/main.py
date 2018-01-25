from Cube import *
from Cylinder import *
from Mesh import *
from Renderer import *


def main():

    polyCube = Cube()
    polyCube.build_polygon_mesh()

    triangleCube = Cube()
    triangleCube.build_triangle_mesh(13)

    randy = Renderer()

    randy.render(polyCube.mesh, 512, "polyCube.jpg")
    randy.render(triangleCube.mesh, 1080, "triangleCube.jpg")


if __name__ == "__main__":
    main()
