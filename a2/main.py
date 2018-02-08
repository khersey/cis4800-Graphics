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
    # cubeMesh.add_transformation(TransformationFactory.scale(0.5,0.5,0.5))
    # cubeMesh.add_transformation(TransformationFactory.z_rotation(45))
    # cubeMesh.add_transformation(TransformationFactory.y_rotation(30))

    myScene = Scene()
    myScene.add_mesh(cubeMesh, (0, 0, 0))

    camera = ViewSystem(myScene)
    camera.build_camera(0.0, 0.0, 4000.0)
    camera.build_view_volume(100.0, 45000.0, 100.0)
    camera.render_scene(1080, "renders/scene.jpg")





if __name__ == "__main__":
    main()
