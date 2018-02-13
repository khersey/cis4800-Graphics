from Cube import *
from Cylinder import *
from Mesh import *
from Renderer import *
from Sphere import *


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

    polySphere = Sphere()
    polySphere.build_polygon_mesh()
    randy.render(polySphere.mesh, 512, "polySphere")

    triangleSphere = Sphere()
    triangleSphere.build_triangle_mesh(4000)
    randy.render(triangleSphere.mesh, 1080, "HDSphere")


if __name__ == "__main__":
    main()
