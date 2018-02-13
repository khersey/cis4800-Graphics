from Cube import *
from Cylinder import *
from Sphere import *
from Mesh import *
from Scene import *
from ViewSystem import *
import TransformationFactory
from mathUtil import *


def main():

    cubeFactory = Cube()
    cubeFactory.build_triangle_mesh(2000)

    cubeMesh = cubeFactory.mesh
    cubeMesh.add_transformation(TransformationFactory.scale(2.0, 2.0, 2.0))
    cubeMesh.add_transformation(TransformationFactory.z_rotation(45))
    cubeMesh.add_transformation(TransformationFactory.x_rotation(45))

    cylinderFactory = Cylinder()
    cylinderFactory.build_triangle_mesh(1350)

    cylndr = cylinderFactory.mesh
    cylndr.add_transformation(TransformationFactory.scale(4.0,4.0,4.0))
    cylndr.add_transformation(TransformationFactory.x_rotation(30))
    cylndr.add_transformation(TransformationFactory.z_rotation(-25))


    scene0 = Scene()
    scene0.add_mesh(cylndr, (0.0, 0.0, -3.0))
    scene0.add_mesh(cubeMesh, (-2.0, -2.0, 1.0))

    # cubeFactory.build_triangle_mesh(300)
    # floor_mesh = cubeFactory.mesh
    # floor_mesh.add_transformation(TransformationFactory.scale(10.0, 10.0, 0.5))

    # myScene.add_mesh(floor_mesh, (0.0, 0.0, -1.0))

    camera = ViewSystem(scene0)
    camera.build_camera(0.0, 20.0, 150.0)
    camera.build_view_volume(23.0, 200.0, 5.0)
    camera.render_scene(1080, "renders/scene.jpg")
    camera.scene.reset()
    
    sphereFactory = Sphere()





if __name__ == "__main__":
    main()
