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

        for index in range(0, len(self.faces)):
            self.faces[index].v1 = solution_dict[self.faces[index].v1]
            self.faces[index].v2 = solution_dict[self.faces[index].v2]
            self.faces[index].v3 = solution_dict[self.faces[index].v3]
            if self.faces[index].v1 == None or self.faces[index].v2 == None or self.faces[index].v3 == None:
                print("ERROR: Face({},{},{}) has unregistered vertexes!!!".format(self.faces[index].v1, self.faces[index].v2, self.faces[index].v3))
            self.faces[index].generate_normal()

        if self.previous_transforms == None:
            self.previous_transforms = self.transform_mtx
        else:
            self.previous_transforms = matrix_multiplication(self.previous_transforms, self.transform_mtx)

        self.transform_mtx = None

    def test_integrity(self):
        print("Mesh Integrity Test")
        print("\nDIAGNOSTICS:")
        print("Faces: {}".format(len(self.faces)))
        print("Edges: {}".format(len(self.edges)))
        print("Vertices: {}".format(len(self.vertices)))

        print("\nTESTS:")
        print("\nAssertion: mesh's face edges match mesh's computed edges in quantity")
        edge_dict = {}
        for face in self.faces:
            for edge in face.get_edges():
                if edge_dict.get(edge) == None:
                    edge_dict[edge] = True

        face_edges = edge_dict.keys()

        edge_dict = {}
        for edge in self.edges:
            if edge_dict.get(edge) == None:
                    edge_dict[edge] = True

        mesh_edges = edge_dict.keys()

        if len(face_edges) == len(mesh_edges):
            print("PASS: {} == {}".format(len(face_edges), len(mesh_edges)))
        else:
            print("FAIL: {} != {}".format(len(face_edges), len(mesh_edges)))

        print("\nAssertion: mesh's face vertices match mesh's computed vertices in quantity")
        v_dict = {}
        for face in self.faces:
            for vertex in face.get_vertices():
                if v_dict.get(vertex) == None:
                    v_dict[vertex] = True

        face_vertices = v_dict.keys()

        v_dict = {}
        for edge in self.edges:
            if v_dict.get(edge[0]) == None:
                v_dict[edge[0]] = True
            if v_dict.get(edge[1]) == None:
                v_dict[edge[1]] = True

        mesh_vertices = v_dict.keys()

        if len(face_vertices) == len(mesh_vertices):
            print("PASS: {} == {}".format(len(face_vertices), len(mesh_vertices)))
        else:
            print("FAIL: {} != {}".format(len(face_vertices), len(mesh_vertices)))

        print("\nAssertion: mesh's computed vertices should all exist in the mesh's face vertices")
        m_dict = {}
        for edge in self.edges:
            if m_dict.get(edge[0]) == None:
                m_dict[edge[0]] = True
            if m_dict.get(edge[1]) == None:
                m_dict[edge[1]] = True

        mesh_vertices = m_dict.keys()

        v_dict = {}
        for face in self.faces:
            for vertex in face.get_vertices():
                if v_dict.get(vertex) == None:
                    v_dict[vertex] = True

        success = True
        for vertex in mesh_vertices:
            if v_dict.get(vertex) == None:
                print("vertex not found in faces: {}".format(vertex))
                success = False

        if success:
            print("PASS: all vertices appear in both faces array and vertices array")
        else:
            print("FAIL: missmatch! see above for more details!")


        print("\nAssertion: mesh's computed vertices should all exist in the mesh's face vertices")
        v_dict = {}
        success = True
        for face in self.faces:
            vertices = face.get_vertices()
            face_has_error = False
            if vertices[0] == vertices[1]:
                face_has_error = True
            elif vertices[0] == vertices[2]:
                face_has_error = True
            elif vertices[2] == vertices[1]:
                face_has_error = True
            
            if face_has_error:
                print("ERROR: face contains 2 identical vertices => Face({},{},{})".format(vertices[0], vertices[1], vertices[2]))
                success = False

        if success:
            print("PASS: no duplicate vertices in this mesh!")
        else:
            print("FAIL: missmatch! see above for more details!")

        