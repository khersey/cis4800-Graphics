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
    cube = cubeFactory.build_triangle_mesh(2000)
    cube.add_transformation(TransformationFactory.scale(2.0, 2.0, 2.0))
    cube.add_transformation(TransformationFactory.z_rotation(45))
    cube.add_transformation(TransformationFactory.x_rotation(45))

    cylinderFactory = Cylinder()
    cylndr = cylinderFactory.build_triangle_mesh(1350)
    cylndr.add_transformation(TransformationFactory.scale(4.0, 4.0, 4.0))
    cylndr.add_transformation(TransformationFactory.x_rotation(30))
    cylndr.add_transformation(TransformationFactory.z_rotation(-25))

    sphereFactory = Sphere()
    sphere = sphereFactory.build_triangle_mesh(4000)
    sphere.add_transformation(TransformationFactory.scale(2.0, 2.0, 5.0))
    sphere.add_transformation(TransformationFactory.y_rotation(35))

    scene0 = Scene()
    scene0.add_mesh(cylndr, (0.0, -1.0, 0.0))
    scene0.add_mesh(cube, (0.0, 1.0, 0.0))
    scene0.add_mesh(sphere, (5.0, 5.0, 1.0))

    # cubeFactory.build_triangle_mesh(300)
    # floor_mesh = cubeFactory.mesh
    # floor_mesh.add_transformation(TransformationFactory.scale(10.0, 10.0, 0.5))

    # myScene.add_mesh(floor_mesh, (0.0, 0.0, -1.0))

    camera = ViewSystem(scene0)
    camera.build_camera(0.0, 0.0, 150.0)
    camera.build_view_volume(23.0, 200.0, 5.0)
    camera.render_scene(1080, "renders/scene0")
    camera.scene.reset()

    sphere1 = sphereFactory.build_triangle_mesh(4000)
    sphere1.add_transformation(TransformationFactory.scale(2.0, 2.0, 5.0))
    sphere1.add_transformation(TransformationFactory.y_rotation(35))

    camera.scene.add_mesh(sphere1, (0.0, 0.0, 0.0))
    camera.build_camera(90.0, 0.0, 40.0)
    camera.build_view_volume(20.0, 500.0, 10.0)
    #camera.render_scene(2160, "renders/scene1")

    basicAssCube = cubeFactory.build_triangle_mesh(128)
    basicAssCube.add_transformation(TransformationFactory.y_rotation(30))
    basicAssCube.add_transformation(TransformationFactory.x_rotation(30))
    basicAssCube.add_transformation(TransformationFactory.z_rotation(30))

    camera.scene.reset()
    camera.build_camera(0.0, 0.0, 10)
    camera.build_view_volume(3.0, 25.0, 2.0)
    camera.scene.add_mesh(basicAssCube, (0.0, 0.0, 0.0))
    # camera.render_scene(900, "renders/cube")

    basicAssCylndr = cylinderFactory.build_triangle_mesh(4000)
    basicAssCylndr.add_transformation(TransformationFactory.y_rotation(30))
    basicAssCylndr.add_transformation(TransformationFactory.x_rotation(30))
    basicAssCylndr.add_transformation(TransformationFactory.z_rotation(30))
    basicAssCylndr.add_transformation(TransformationFactory.scale(4.0, 4.0, 4.0))

    camera.scene.reset()
    camera.build_camera(25.0, 25.0, 8.0)
    camera.build_view_volume(3.0, 25.0, 2.0)
    camera.scene.add_mesh(basicAssCylndr, (0.0, 0.0, 0.0))
    camera.render_scene(2000, "renders/cylinder")

    basicAssSphere = sphereFactory.build_polygon_mesh()
    basicAssSphere.add_transformation(TransformationFactory.y_rotation(30))
    basicAssSphere.add_transformation(TransformationFactory.x_rotation(30))
    basicAssSphere.add_transformation(TransformationFactory.z_rotation(30))

    camera.scene.reset()
    camera.build_camera(20.0, 50.0, 10.0)
    camera.build_view_volume(3.0, 25.0, 2.0)
    camera.scene.add_mesh(basicAssSphere, (0.0, 0.0, 0.0))
    camera.render_scene(900, "renders/sphere")



if __name__ == "__main__":
    main()
