from Mesh import *

class Cube:

    def __init__(self):
        self.mesh = None

    def build_polygon_mesh(self):
        self.build_triangle_mesh(1)

    def build_triangle_mesh(self, resolution):
        n = 1
        output = 12
        while output < resolution:
            n += 1
            output = 12 * (n * n) 

        m = Mesh()

        v_dict = {}
        
        # create all vertices
        for first in range(0, n+1):
            for second in range(0, n+1):
                i = (2.0 / float(n)) * first - 1.0
                j = (2.0 / float(n)) * second - 1.0

                # z = 1
                coordinates = (i, j, 1)
                if v_dict.get(coordinates) == None:
                    v_dict[coordinates] = True
                    m.vertices.append(coordinates)

                # z = -1
                coordinates = (i, j, -1)
                if v_dict.get(coordinates) == None:
                    v_dict[coordinates] = True
                    m.vertices.append(coordinates)

                # y = 1 
                coordinates = (i, 1, j)
                if v_dict.get(coordinates) == None:
                    v_dict[coordinates] = True
                    m.vertices.append(coordinates)

                # y = -1
                coordinates = (i, -1, j)
                if v_dict.get(coordinates) == None:
                    v_dict[coordinates] = True
                    m.vertices.append(coordinates)

                # x = 1
                coordinates = (1, i, j)
                if v_dict.get(coordinates) == None:
                    v_dict[coordinates] = True
                    m.vertices.append(coordinates)
            
                # x = -1
                coordinates = (-1, i, j)
                if v_dict.get(coordinates) == None:
                    v_dict[coordinates] = True
                    m.vertices.append(coordinates)

        v_dict.clear() # free ram

        e_dict = {}

        # create edges
        for first in range(0, n+1):
            for second in range(0, n+1):
                i = float((2.0 / float(n)) * first - 1.0)
                j = float((2.0 / float(n)) * second - 1.0)

                i_plus1 = float((2.0 / float(n)) * (1.0 + first) - 1.0)
                j_plus1 = float((2.0 / float(n)) * (1.0 + second) - 1.0)

                # z = 1
                coordinates = (i, j, 1.0)
                horizontal  = (i_plus1, j, 1.0)
                vertical    = (i, j_plus1, 1.0)
                diagonal    = (i_plus1, j_plus1, 1.0)
                if first != n and e_dict.get( (coordinates, horizontal) ) == None:
                    e_dict[ (coordinates, horizontal) ] = True
                    m.edges.append( (coordinates, horizontal) )
                    
                if second != n and e_dict.get( (coordinates, vertical) ) == None:
                    e_dict[ (coordinates, vertical) ] = True
                    m.edges.append( (coordinates, vertical) )
                
                if first != n and second != n and e_dict.get( (coordinates, diagonal) ) == None:
                    e_dict[ (coordinates, diagonal) ] = True
                    m.edges.append( (coordinates, diagonal) )

                # z = -1
                coordinates = (i, j, -1.0)
                horizontal  = (i_plus1, j, -1.0)
                vertical    = (i, j_plus1, -1.0)
                diagonal    = (i_plus1, j_plus1, -1.0)
                if first != n and e_dict.get( (coordinates, horizontal) ) == None:
                    e_dict[ (coordinates, horizontal) ] = True
                    m.edges.append( (coordinates, horizontal) )
                    
                if second != n and e_dict.get( (coordinates, vertical) ) == None:
                    e_dict[ (coordinates, vertical) ] = True
                    m.edges.append( (coordinates, vertical) )
                
                if first != n and second != n and e_dict.get( (coordinates, diagonal) ) == None:
                    e_dict[ (coordinates, diagonal) ] = True
                    m.edges.append( (coordinates, diagonal) )

                # y = 1 
                coordinates = (i, 1.0, j)
                horizontal  = (i_plus1, 1.0, j)
                vertical    = (i, 1.0, j_plus1)
                diagonal    = (i_plus1, 1.0, j_plus1)
                if first != n and e_dict.get( (coordinates, horizontal) ) == None:
                    e_dict[ (coordinates, horizontal) ] = True
                    m.edges.append( (coordinates, horizontal) )
                    
                if second != n and e_dict.get( (coordinates, vertical) ) == None:
                    e_dict[ (coordinates, vertical) ] = True
                    m.edges.append( (coordinates, vertical) )
                
                if first != n and second != n and e_dict.get( (coordinates, diagonal) ) == None:
                    e_dict[ (coordinates, diagonal) ] = True
                    m.edges.append( (coordinates, diagonal) )

                # y = -1
                coordinates = (i, -1.0, j)
                horizontal  = (i_plus1, -1.0, j)
                vertical    = (i, -1.0, j_plus1)
                diagonal    = (i_plus1, -1.0, j_plus1)
                if first != n and e_dict.get( (coordinates, horizontal) ) == None:
                    e_dict[ (coordinates, horizontal) ] = True
                    m.edges.append( (coordinates, horizontal) )
                    
                if second != n and e_dict.get( (coordinates, vertical) ) == None:
                    e_dict[ (coordinates, vertical) ] = True
                    m.edges.append( (coordinates, vertical) )
                
                if first != n and second != n and e_dict.get( (coordinates, diagonal) ) == None:
                    e_dict[ (coordinates, diagonal) ] = True
                    m.edges.append( (coordinates, diagonal) )

                # x = 1
                coordinates = (1.0, i, j)
                horizontal  = (1.0, i_plus1, j)
                vertical    = (1.0, i, j_plus1)
                diagonal    = (1.0, i_plus1, j_plus1)
                if first != n and e_dict.get( (coordinates, horizontal) ) == None:
                    e_dict[ (coordinates, horizontal) ] = True
                    m.edges.append( (coordinates, horizontal) )
                    
                if second != n and e_dict.get( (coordinates, vertical) ) == None:
                    e_dict[ (coordinates, vertical) ] = True
                    m.edges.append( (coordinates, vertical) )
                
                if first != n and second != n and e_dict.get( (coordinates, diagonal) ) == None:
                    e_dict[ (coordinates, diagonal) ] = True
                    m.edges.append( (coordinates, diagonal) )
            
                # x = -1
                coordinates = (-1.0, i, j)
                horizontal  = (-1.0, i_plus1, j)
                vertical    = (-1.0, i, j_plus1)
                diagonal    = (-1.0, i_plus1, j_plus1)
                if first != n and e_dict.get( (coordinates, horizontal) ) == None:
                    e_dict[ (coordinates, horizontal) ] = True
                    m.edges.append( (coordinates, horizontal) )
                    
                if second != n and e_dict.get( (coordinates, vertical) ) == None:
                    e_dict[ (coordinates, vertical) ] = True
                    m.edges.append( (coordinates, vertical) )
                
                if first != n and second != n and e_dict.get( (coordinates, diagonal) ) == None:
                    e_dict[ (coordinates, diagonal) ] = True
                    m.edges.append( (coordinates, diagonal) )

        self.mesh = m
            
