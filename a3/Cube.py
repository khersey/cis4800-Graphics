from Mesh import *
from Face import *

class Cube:

    def __init__(self):
        pass

    def build_polygon_mesh(self):
        mesh = self.build_triangle_mesh(1)
        return mesh

    def build_triangle_mesh(self, resolution):
        n = 1
        output = 12
        while output < resolution:
            n += 1
            output = 12 * (n * n) 

        mesh = Mesh()

        v_dict = {}
        e_dict = {}

        # create edges and vertices
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
                if v_dict.get(coordinates) == None:
                    v_dict[coordinates] = True
                    mesh.vertices.append(coordinates)

                if first != n and e_dict.get( (coordinates, horizontal) ) == None:
                    e_dict[ (coordinates, horizontal) ] = True
                    mesh.edges.append( (coordinates, horizontal) )
                    
                if second != n and e_dict.get( (coordinates, vertical) ) == None:
                    e_dict[ (coordinates, vertical) ] = True
                    mesh.edges.append( (coordinates, vertical) )
                
                if first != n and second != n and e_dict.get( (coordinates, diagonal) ) == None:
                    e_dict[ (coordinates, diagonal) ] = True
                    mesh.edges.append( (coordinates, diagonal) )

                # add faces
                if first != n and second != n:
                    mesh.faces.append(Face(coordinates, diagonal, vertical))
                    mesh.faces.append(Face(diagonal, coordinates, horizontal))


                # z = -1
                coordinates = (i, j, -1.0)
                horizontal  = (i_plus1, j, -1.0)
                vertical    = (i, j_plus1, -1.0)
                diagonal    = (i_plus1, j_plus1, -1.0)
                if v_dict.get(coordinates) == None:
                    v_dict[coordinates] = True
                    mesh.vertices.append(coordinates)

                if first != n and e_dict.get( (coordinates, horizontal) ) == None:
                    e_dict[ (coordinates, horizontal) ] = True
                    mesh.edges.append( (coordinates, horizontal) )
                    
                if second != n and e_dict.get( (coordinates, vertical) ) == None:
                    e_dict[ (coordinates, vertical) ] = True
                    mesh.edges.append( (coordinates, vertical) )
                
                if first != n and second != n and e_dict.get( (coordinates, diagonal) ) == None:
                    e_dict[ (coordinates, diagonal) ] = True
                    mesh.edges.append( (coordinates, diagonal) )
                
                # add faces
                if first != n and second != n:
                    mesh.faces.append(Face(coordinates, vertical, diagonal))
                    mesh.faces.append(Face(diagonal, horizontal, coordinates))
                    # other
                    
                

                # y = 1 
                coordinates = (i, 1.0, j)
                horizontal  = (i_plus1, 1.0, j)
                vertical    = (i, 1.0, j_plus1)
                diagonal    = (i_plus1, 1.0, j_plus1)
                if v_dict.get(coordinates) == None:
                    v_dict[coordinates] = True
                    mesh.vertices.append(coordinates)

                if first != n and e_dict.get( (coordinates, horizontal) ) == None:
                    e_dict[ (coordinates, horizontal) ] = True
                    mesh.edges.append( (coordinates, horizontal) )
                    
                if second != n and e_dict.get( (coordinates, vertical) ) == None:
                    e_dict[ (coordinates, vertical) ] = True
                    mesh.edges.append( (coordinates, vertical) )
                
                if first != n and second != n and e_dict.get( (coordinates, diagonal) ) == None:
                    e_dict[ (coordinates, diagonal) ] = True
                    mesh.edges.append( (coordinates, diagonal) )

                # add faces
                if first != n and second != n:
                    mesh.faces.append(Face(coordinates, vertical, diagonal))
                    mesh.faces.append(Face(diagonal, horizontal, coordinates))
                    
                    


                # y = -1
                coordinates = (i, -1.0, j)
                horizontal  = (i_plus1, -1.0, j)
                vertical    = (i, -1.0, j_plus1)
                diagonal    = (i_plus1, -1.0, j_plus1)
                if v_dict.get(coordinates) == None:
                    v_dict[coordinates] = True
                    mesh.vertices.append(coordinates)

                if first != n and e_dict.get( (coordinates, horizontal) ) == None:
                    e_dict[ (coordinates, horizontal) ] = True
                    mesh.edges.append( (coordinates, horizontal) )
                    
                if second != n and e_dict.get( (coordinates, vertical) ) == None:
                    e_dict[ (coordinates, vertical) ] = True
                    mesh.edges.append( (coordinates, vertical) )
                
                if first != n and second != n and e_dict.get( (coordinates, diagonal) ) == None:
                    e_dict[ (coordinates, diagonal) ] = True
                    mesh.edges.append( (coordinates, diagonal) )

                # add faces
                if first != n and second != n:
                    mesh.faces.append(Face(coordinates, diagonal, vertical))
                    mesh.faces.append(Face(diagonal, coordinates, horizontal))


                # x = 1
                coordinates = (1.0, i, j)
                horizontal  = (1.0, i_plus1, j)
                vertical    = (1.0, i, j_plus1)
                diagonal    = (1.0, i_plus1, j_plus1)
                if v_dict.get(coordinates) == None:
                    v_dict[coordinates] = True
                    mesh.vertices.append(coordinates)

                if first != n and e_dict.get( (coordinates, horizontal) ) == None:
                    e_dict[ (coordinates, horizontal) ] = True
                    mesh.edges.append( (coordinates, horizontal) )
                    
                if second != n and e_dict.get( (coordinates, vertical) ) == None:
                    e_dict[ (coordinates, vertical) ] = True
                    mesh.edges.append( (coordinates, vertical) )
                
                if first != n and second != n and e_dict.get( (coordinates, diagonal) ) == None:
                    e_dict[ (coordinates, diagonal) ] = True
                    mesh.edges.append( (coordinates, diagonal) )
                
                # add faces
                if first != n and second != n:
                    mesh.faces.append(Face(coordinates, diagonal, vertical))
                    mesh.faces.append(Face(diagonal, coordinates, horizontal))
            
                # x = -1
                coordinates = (-1.0, i, j)
                horizontal  = (-1.0, i_plus1, j)
                vertical    = (-1.0, i, j_plus1)
                diagonal    = (-1.0, i_plus1, j_plus1)
                if v_dict.get(coordinates) == None:
                    v_dict[coordinates] = True
                    mesh.vertices.append(coordinates)

                if first != n and e_dict.get( (coordinates, horizontal) ) == None:
                    e_dict[ (coordinates, horizontal) ] = True
                    mesh.edges.append( (coordinates, horizontal) )
                    
                if second != n and e_dict.get( (coordinates, vertical) ) == None:
                    e_dict[ (coordinates, vertical) ] = True
                    mesh.edges.append( (coordinates, vertical) )
                
                if first != n and second != n and e_dict.get( (coordinates, diagonal) ) == None:
                    e_dict[ (coordinates, diagonal) ] = True
                    mesh.edges.append( (coordinates, diagonal) )

                # add faces
                if first != n and second != n:
                    mesh.faces.append(Face(coordinates, vertical, diagonal))
                    mesh.faces.append(Face(diagonal, horizontal, coordinates))

        return mesh
            
