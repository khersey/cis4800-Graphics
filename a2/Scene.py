from Mesh import *
import TransformationFactory

class Scene:
    def __init__(self):
        self.models = []
        self.coordinates = [] # (x,y,z) tuples, indexes matching the above meshes

    def add_mesh(self, mesh, pos):
        mesh.add_transformation(TransformationFactory.translation(float(pos[0]), float(pos[1]), float(pos[2])))
        mesh.apply_transformations()
        self.models.append(mesh)
        self.coordinates.append(pos)