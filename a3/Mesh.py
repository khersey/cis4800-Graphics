from mathUtil import *

class Mesh:
    def __init__(self):
        # vertex = (x,y,z)
        self.vertices = [] 
        # edge = ((x1,y1,z1), (x2,y2,z2))
        self.edges = []
        # face = Face((x1,y1,z1), (x2,y2,z2), (x3,y3,z3), (r,g,b))
        self.faces = []

        self.transform_mtx = None
        self.previous_transforms = None

    def add_transformation(self, transformation):
        if self.transform_mtx == None:
            self.transform_mtx = transformation
        else:
            self.transform_mtx = matrix_multiplication(self.transform_mtx, transformation)
    
    def apply_transformations(self):
        if self.transform_mtx == None:
            return

        solution_dict = {}

        for index in range(0, len(self.vertices)):
            vertex = self.vertices[index]
            new_vertex = apply_transformation(vertex, self.transform_mtx)
            solution_dict[vertex] = new_vertex
            self.vertices[index] = new_vertex

        for index in range(0, len(self.edges)):
            edge = self.edges[index]
            first = solution_dict.get(edge[0])
            second = solution_dict.get(edge[1])
            if first == None or second == None:
                print("ERROR: edge(" + str(edge[0]) + ", " + str(edge[1]) + ") has an unregistered vertex!")
            self.edges[index] = (first, second)

        if self.previous_transforms == None:
            self.previous_transforms = self.transform_mtx
        else:
            self.previous_transforms = matrix_multiplication(self.previous_transforms, self.transform_mtx)

        self.transform_mtx = None
