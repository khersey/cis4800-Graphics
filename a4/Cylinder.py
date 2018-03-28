from Mesh import *
from Face import *

from math import *
from mathUtil import *

class Cylinder:

    def __init__(self):
        pass

    def build_polygon_mesh(self):
        mesh = self.build_triangle_mesh(1)
        return mesh

    def build_triangle_mesh(self, resolution):  
        n = 6.0
        output = 30.0
        h = int(n/2) + 1 #height

        while output < resolution:
            n += 1.0
            h = int(n/2) + 1
            output = 2 * n + (n * h) 
        
        mesh = Mesh()

        # center vertices
        v_bottom = (0.0, -1.0, 0.0)
        v_top = (0.0, 1.0, 0.0)

        # edge and vertex dictionaries
        e_dict = {}
        v_dict = {}

        for first in range(0, int(n+1)): # around
            for second in range(0, h+1): # height

                x = cos( ((2.0 * pi) / n) * first )
                y = (2.0 / h) * float(second) - 1.0
                z = sin( ((2.0 * pi) / n) * first )

                x_iPlus1 = cos( ((2.0 * pi) / n) * (first + 1) )
                y_jPlus1 = (2.0 / h) * float(second + 1) - 1.0
                z_iPlus1 = sin( ((2.0 * pi) / n) * (first + 1) )

                coordinates = (x, y, z)
                vertical    = (x, y_jPlus1, z)
                horizontal  = (x_iPlus1, y, z_iPlus1)
                diagonal    = (x_iPlus1, y_jPlus1, z_iPlus1)

                # if top
                if y == 1.0 and e_dict.get( (coordinates, v_top) ) == None:
                    e_dict[ (coordinates, v_top) ] = True
                    mesh.edges.append( (coordinates, v_top) )

                    if v_dict.get(coordinates) == None:
                        v_dict[coordinates] = True
                        mesh.vertices.append(coordinates)

                    if v_dict.get(v_top) == None:
                        v_dict[v_top] = True
                        mesh.vertices.append(v_top)

                    # add face
                    mesh.faces.append(Face(v_top, horizontal, coordinates))

                # if bottom
                if y == -1.0 and e_dict.get( (coordinates, v_bottom) ) == None:
                    e_dict[ (coordinates, v_bottom) ] = True
                    mesh.edges.append( (coordinates, v_bottom) )
 
                    if v_dict.get(coordinates) == None:
                        v_dict[coordinates] = True
                        mesh.vertices.append(coordinates)

                    if v_dict.get(v_bottom) == None:
                        v_dict[v_bottom] = True
                        mesh.vertices.append(v_bottom)
                    
                    # add face
                    mesh.faces.append(Face(v_bottom, coordinates, horizontal))

                # horizontal
                if e_dict.get( (coordinates, horizontal) ) == None:
                    e_dict[ (coordinates, horizontal) ] = True
                    mesh.edges.append( (coordinates, horizontal) )

                    if v_dict.get(coordinates) == None:
                        v_dict[coordinates] = True
                        mesh.vertices.append(coordinates)

                    if v_dict.get(horizontal) == None:
                        v_dict[horizontal] = True
                        mesh.vertices.append(horizontal)
                    
                # vertical
                if y_jPlus1 <= 1.0 and e_dict.get( (coordinates, vertical) ) == None:
                    e_dict[ (coordinates, vertical) ] = True
                    mesh.edges.append( (coordinates, vertical) )

                    if v_dict.get(coordinates) == None:
                        v_dict[coordinates] = True
                        mesh.vertices.append(coordinates)

                    if v_dict.get(vertical) == None:
                        v_dict[vertical] = True
                        mesh.vertices.append(vertical)
                
                # diagonal
                if y_jPlus1 <= 1.0 and e_dict.get( (coordinates, diagonal) ) == None:
                    e_dict[ (coordinates, diagonal) ] = True
                    mesh.edges.append( (coordinates, diagonal) )

                    if v_dict.get(coordinates) == None:
                        v_dict[coordinates] = True
                        mesh.vertices.append(coordinates)

                    if v_dict.get(diagonal) == None:
                        v_dict[diagonal] = True
                        mesh.vertices.append(diagonal)
                
                # add faces
                if y != 1.0:
                    mesh.faces.append(Face(coordinates, vertical, diagonal))
                    mesh.faces.append(Face(diagonal, horizontal, coordinates))

        return mesh
