from Mesh import *

class Scene:
    def __init__(self):
        self.meshes = []
        self.meshCoordinates = [] # (x,y,z) tuples, indexes matching the above meshes

    def add_mesh(self, mesh, coordinates):
        mesh.apply_transformatons()
        self.meshes.append(mesh)
        self.meshCoordinates.append(coordinates)