from Mesh import *
from math import *
from Face import *

class Sphere:

    def __init__(self):
        pass

    def build_polygon_mesh(self):
        mesh = self.build_triangle_mesh(1)
        return mesh

    def build_triangle_mesh(self, resolution):

        w = 8
        h = 8
        my_res = (2 * w) + (2 * w * (h - 2))

        while my_res < resolution:
            w += 1
            my_res = (2 * w) + (2 * w * (h - 2))
            if my_res < resolution:
                h += 1
                my_res = (2 * w) + (2 * w * (h - 2))

        # scaling function

        mesh = Mesh()

        v_dict = {}
        e_dict = {} 
        # TODO: these dictionaries might be redudant here

        # center vertices
        v_bottom = (0.0, -1.0, 0.0)
        v_top = (0.0, 1.0, 0.0)

        for height in range(0, h):
            for around in range(0, w): # points around the sphere

                x = sin(pi * (around/w)) * cos(2*pi * (height/h))
                y = sin(pi * (around/w)) * sin(2*pi * (height/h))
                z = cos(pi * (around/w))

                x_hor = sin(pi * ((around + 1)/w)) * cos(2*pi * (height/h))
                x_ver = sin(pi * (around/w)) * cos(2*pi * ((height+1)/h))
                x_diag = sin(pi * ((around + 1)/w)) * cos(2*pi * ((height+1)/h))
                y_hor = sin(pi * ((around+1)/w)) * sin(2*pi * (height/h))
                y_ver = sin(pi * (around/w)) * sin(2*pi * ((height+1)/h))
                y_diag = sin(pi * ((around+1)/w)) * sin(2*pi * ((height+1)/h))
                z_plus1 = cos(pi * ((around + 1)/w))

                coordinates = (x, y, z)
                vertical    = (x_ver, y_ver, z)
                horizontal  = (x_hor, y_hor, z_plus1)
                diagonal    = (x_diag, y_diag, z_plus1)

                if v_dict.get(coordinates) == None:
                        v_dict[coordinates] = True
                        mesh.vertices.append(coordinates)

                if y == -1.0: # bottom tip
                    coordinates = v_bottom

                    if v_dict.get(coordinates) == None:
                        v_dict[coordinates] = True
                        mesh.vertices.append(coordinates)

                    if v_dict.get(vertical) == None:
                        v_dict[coordinates] = True
                        mesh.vertices.append(vertical)

                    if e_dict.get( (coordinates, vertical) ) == None:
                        e_dict[ (coordinates, vertical) ] = True
                        mesh.edges.append( (coordinates, vertical) )

                    natural = cross_product(vector_from_points(horizontal, vertical), vector_from_points(horizontal, coordinates))
                    mesh.faces.append(Face(coordinates, vertical, diagonal, natural))

                elif y_ver == 1.0: # one row below the top 
                    vertical = v_top

                    if e_dict.get( (coordinates, vertical) ) == None:
                        e_dict[ (coordinates, vertical) ] = True
                        mesh.edges.append( (coordinates, vertical) )

                    natural = cross_product(vector_from_points(diagonal, vertical), vector_from_points(diagonal, coordinates))
                    mesh.faces.append(Face(coordinates, vertical, horizontal, natural))


                elif y == 1.0: # top tip
                    coordinates = v_top

                    if v_dict.get(coordinates) == None:
                        v_dict[coordinates] = True
                        mesh.vertices.append(coordinates)
                    # no faces for top tip

                else: # normal polygon
                    if v_dict.get(vertical) == None:
                        v_dict[coordinates] = True
                        mesh.vertices.append(vertical)

                    if v_dict.get(horizontal) == None:
                        v_dict[coordinates] = True
                        mesh.vertices.append(horizontal)

                    if v_dict.get(diagonal) == None:
                        v_dict[coordinates] = True
                        mesh.vertices.append(diagonal)

                    if e_dict.get( (coordinates, vertical) ) == None:
                        e_dict[ (coordinates, vertical) ] = True
                        mesh.edges.append( (coordinates, vertical) )

                    if e_dict.get( (coordinates, horizontal) ) == None:
                        e_dict[ (coordinates, horizontal) ] = True
                        mesh.edges.append( (coordinates, horizontal) )

                    if e_dict.get( (coordinates, diagonal) ) == None:
                        e_dict[ (coordinates, diagonal) ] = True
                        mesh.edges.append( (coordinates, diagonal) )

                    natural = cross_product(vector_from_points(horizontal, coordinates), vector_from_points(horizontal, diagonal))
                    mesh.faces.append(Face(coordinates, vertical, diagonal, natural))
                    mesh.faces.append(Face(coordinates, horizontal, diagonal, natural))

        return mesh

