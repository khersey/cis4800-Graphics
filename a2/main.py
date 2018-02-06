from Cube import *
from Cylinder import *
from Mesh import *
from Renderer import *
import TransformationFactory


def main():
    randy = Renderer()

    # polyCube = Cube()
    # polyCube.build_polygon_mesh()
    # randy.render(polyCube.mesh, 512, "polyCube.jpg")

    triangleCube = Cube()
    triangleCube.build_triangle_mesh(24)

    cubeMesh = triangleCube.mesh
    cubeMesh.add_transformation(TransformationFactory.scale(0.5,0.5,0.5))
    cubeMesh.add_transformation(TransformationFactory.z_rotation(45))
    cubeMesh.add_transformation(TransformationFactory.y_rotation(30))
    cubeMesh.apply_transformations()

    randy.render(cubeMesh, 1080, "HDcube.jpg")

    # polyCylinder = Cylinder()
    # polyCylinder.build_polygon_mesh()
    # randy.render(polyCylinder.mesh, 512, "polyCylinder.jpg")

    # triangleCylinder = Cylinder()
    # triangleCylinder.build_triangle_mesh(4000)
    # randy.render(triangleCylinder.mesh, 1080, "HDcylinder.jpg")


if __name__ == "__main__":
    main()
