from Mesh import *
from math import *

class Cylinder:

    def __init__(self):
        self.mesh = None

    def build_polygon_mesh(self):
        self.build_triangle_mesh(1)

    def build_triangle_mesh(self, resolution):  
        n = 6
        output = 48

        while output < resolution:
            n += 1
            output = 2 * n + (n * n) 

        # add scaling

        v_dict = {}
        m = Mesh()

        # first add center vertices
        v_bottom = (0, -1, 0)
        m.vertices.append(v_bottom)
        v_dict[v_bottom] = True

        v_top = (0, 1, 0)
        m.vertices.append(v_top)
        v_dict[v_top] = True

        # the rest of the vertices
        for first in range(0, n+1):
            for second in range(0, n+1):
                x = cos( ((2 * pi) / n) * first )
                y = (2.0 / (n / 2)) * float(second) - 1.0 
                z = sin( ((2 * pi) / n) * first )

                coordinates = (x,y,z)
                if v_dict.get(coordinates) == None:
                    v_dict[coordinates] = True
                    m.vertices.append(coordinates)

        # edges
        e_dict = {}

        for first in range(0, n+1):
            for second in range(0, n+1):
                x = cos( ((2 * pi) / n) * first )
                y = (2.0 / (n / 2)) * float(second) - 1.0
                z = sin( ((2 * pi) / n) * first )

                x_iPlus1 = cos( ((2 * pi) / n) * (first + 1) )
                y_jPlus1 = (2.0 / (n / 2)) * float(second + 1) - 1.0
                z_iPlus1 = sin( ((2 * pi) / n) * (first + 1) )

                coordinates = (x, y, z)
                vertical    = (x, y_jPlus1, z)
                horizontal  = (x_iPlus1, y, z_iPlus1)
                diagonal    = (x_iPlus1, y_jPlus1, z_iPlus1)

                # if top
                if y == 1 and e_dict.get( (coordinates, v_top) ) == None:
                    e_dict[ (coordinates, v_top) ] = True
                    m.edges.append( (coordinates, v_top) )

                # if bottom
                if y == -1 and e_dict.get( (coordinates, v_bottom) ) == None:
                    e_dict[ (coordinates, v_bottom) ] = True
                    m.edges.append( (coordinates, v_bottom) )

                # horizontal
                if e_dict.get( (coordinates, horizontal) ) == None:
                    e_dict[ (coordinates, horizontal) ] = True
                    m.edges.append( (coordinates, horizontal) )
                    
                # vertical
                if y_jPlus1 <= 1 and e_dict.get( (coordinates, vertical) ) == None:
                    e_dict[ (coordinates, vertical) ] = True
                    m.edges.append( (coordinates, vertical) )
                
                # diagonal
                if y_jPlus1 <= 1 and e_dict.get( (coordinates, diagonal) ) == None:
                    e_dict[ (coordinates, diagonal) ] = True
                    m.edges.append( (coordinates, diagonal) )

        self.mesh = m





