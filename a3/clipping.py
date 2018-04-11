from Face import *

def clip(face_list):
    new_face_list = []
    for index in range(0, len(face_list)):
        face = face_list[index]
        vertices = []
        for edge in face.get_edges():
            m = edge[0]
            n = edge[1]
            m_inside = is_inside(m)
            n_inside = is_inside(n)

            if m_inside and n_inside:
                vertices.append(n)
            elif m_inside and not n_inside:
                vertices.append(find_intersection((m,n)))
            elif not m_inside and n_inside:
                vertices.append(find_intersection((n,m)))
                vertices.append(n)

        if len(vertices) == 3:
            face.v1 = vertices[0]
            face.v2 = vertices[1]
            face.v3 = vertices[2]
            new_face_list.append(face)
        elif len(vertices) == 4:
            # TODO: change order to make phong shading work
            face.v1 = vertices[0]
            face.v2 = vertices[1]
            face.v3 = vertices[2]
            new_face_list.append(face)
            face2 = Face(vertices[0], vertices[2], vertices[3], face.rgb)
            new_face_list.append(face2)

            

    return new_face_list

def is_inside(vertex):
    x = vertex[0]
    y = vertex[1]
    z = vertex[2]

    x_in = x <= 1.0 and x >= -1.0
    y_in = y <= 1.0 and y >= -1.0
    z_in = z <= 1.0 and z >= 0.0

    res = x_in and y_in and z_in
    return res

def find_intersection(edge):
    inside = edge[0]
    outside = edge[1]

    if not (outside[0] <= 1.0 and outside[0] >= -1.0): # x outside
        new_x = 1.0 
        if outside[0] < -1.0:
            new_x = -1.0
        
        scale = (new_x - inside[0]) / (outside[0] - inside[0])

        new_y = inside[1] + (scale * (outside[1] - inside[1]))
        new_z = inside[2] + (scale * (outside[2] - inside[2]))

        outside = (new_x, new_y, new_z)

    if not (outside[1] <= 1.0 and outside[1] >= -1.0):
        new_y = 1.0 
        if outside[1] < -1.0:
            new_y = -1.0
        
        scale = (new_y - inside[1]) / (outside[1] - inside[1])

        new_x = inside[0] + (scale * (outside[0] - inside[0]))
        new_z = inside[2] + (scale * (outside[2] - inside[2]))

        outside = (new_x, new_y, new_z)

    if not (outside[2] <= 1.0 and outside[2] >= 0.0):
        new_z = 1.0 
        if outside[2] < 0.0:
            new_z = 0.0
        
        scale = (new_z - inside[2]) / (outside[2] - inside[2])

        new_x = inside[0] + (scale * (outside[0] - inside[0]))
        new_y = inside[1] + (scale * (outside[1] - inside[1]))

        outside = (new_x, new_y, new_z)

    return outside