from Cube import *
from Cylinder import *
from Mesh import *
from Scene import *
from ViewSystem import *
import TransformationFactory
from mathUtil import *


def main():

    cubeFactory = Cube()
    cubeFactory.build_triangle_mesh(1)

    cubeMesh = cubeFactory.mesh
    cubeMesh.add_transformation(TransformationFactory.scale(2.0, 2.0, 2.0))
    cubeMesh.add_transformation(TransformationFactory.z_rotation(45))
    cubeMesh.add_transformation(TransformationFactory.x_rotation(45))

    cylinderFactory = Cylinder()
    cylinderFactory.build_triangle_mesh(4000)

    mesh = cylinderFactory.mesh
    mesh.add_transformation(TransformationFactory.scale(4.0,4.0,4.0))
    mesh.add_transformation(TransformationFactory.x_rotation(30))
    mesh.add_transformation(TransformationFactory.z_rotation(-25))


    myScene = Scene()
    myScene.add_mesh(mesh, (0.0, 0.0, 0.0))
    #myScene.add_mesh(cubeMesh, (-2.0, -2.0, 1.0))

    # cubeFactory.build_triangle_mesh(300)
    # floor_mesh = cubeFactory.mesh
    # floor_mesh.add_transformation(TransformationFactory.scale(10.0, 10.0, 0.5))

    # myScene.add_mesh(floor_mesh, (0.0, 0.0, -1.0))

    camera = ViewSystem(myScene)
    camera.build_camera(0.0, 0.0, 30.0)
    camera.build_view_volume(25.0, 200.0, 15.0)
    camera.render_scene(1080, "renders/scene.jpg")





if __name__ == "__main__":
    main()
