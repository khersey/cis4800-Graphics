from Mesh import *
from math import *

class Cylinder:

    def __init__(self):
        self.mesh = None

    def build_polygon_mesh(self):
        self.build_triangle_mesh(1)

    def build_triangle_mesh(self, resolution):  
        n = 6.0
        output = 30.0
        h = int(n/2) + 1 #height

        while output < resolution:
            n += 1.0
            h = int(n/2) + 1
            output = 2 * n + (n * h) 
        
        m = Mesh()

        # center vertices
        v_bottom = (0.0, -1.0, 0.0)
        v_top = (0.0, 1.0, 0.0)

        # edge and vertex dictionaries
        e_dict = {}
        v_dict = {}

        for first in range(0, int(n+1)):
            for second in range(0, h+1): 

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
                    m.edges.append( (coordinates, v_top) )

                    if v_dict.get(coordinates) == None:
                        v_dict[coordinates] = True
                        m.vertices.append(coordinates)

                    if v_dict.get(v_top) == None:
                        v_dict[v_top] = True
                        m.vertices.append(v_top)

                # if bottom
                if y == -1.0 and e_dict.get( (coordinates, v_bottom) ) == None:
                    e_dict[ (coordinates, v_bottom) ] = True
                    m.edges.append( (coordinates, v_bottom) )
 
                    if v_dict.get(coordinates) == None:
                        v_dict[coordinates] = True
                        m.vertices.append(coordinates)

                    if v_dict.get(v_bottom) == None:
                        v_dict[v_bottom] = True
                        m.vertices.append(v_bottom)

                # horizontal
                if e_dict.get( (coordinates, horizontal) ) == None:
                    e_dict[ (coordinates, horizontal) ] = True
                    m.edges.append( (coordinates, horizontal) )

                    if v_dict.get(coordinates) == None:
                        v_dict[coordinates] = True
                        m.vertices.append(coordinates)

                    if v_dict.get(horizontal) == None:
                        v_dict[horizontal] = True
                        m.vertices.append(horizontal)
                    
                # vertical
                if y_jPlus1 <= 1.0 and e_dict.get( (coordinates, vertical) ) == None:
                    e_dict[ (coordinates, vertical) ] = True
                    m.edges.append( (coordinates, vertical) )

                    if v_dict.get(coordinates) == None:
                        v_dict[coordinates] = True
                        m.vertices.append(coordinates)

                    if v_dict.get(vertical) == None:
                        v_dict[vertical] = True
                        m.vertices.append(vertical)
                
                # diagonal
                if y_jPlus1 <= 1.0 and e_dict.get( (coordinates, diagonal) ) == None:
                    e_dict[ (coordinates, diagonal) ] = True
                    m.edges.append( (coordinates, diagonal) )

                    if v_dict.get(coordinates) == None:
                        v_dict[coordinates] = True
                        m.vertices.append(coordinates)

                    if v_dict.get(diagonal) == None:
                        v_dict[diagonal] = True
                        m.vertices.append(diagonal)

        self.mesh = m