from math import *

from mathUtil import *
from Renderer import *
from Mesh import *
from Scene import *
from Face import *

class ViewSystem:

    def __init__(self, scene):
        self.scene = scene

        self.elevation_angle = None # in radians
        self.rotation_angle = None  # in radians
        self.radial_distance = None 

        self.d = 0 # near plane distance
        self.f = 0 # far plane distnace
        self.h = 0 # height / width of view plane

        self.near_plane = None # 4-tuple of 3-tuples
        # NEAR PLANE
        # (
        #    ( h, -h, d), top left corner
        #    ( h,  h, d), top right corner
        #    (-h,  h, d), bottom right corner
        #    (-h, -h, d)  bottom left corner
        # )

        self.far_plane = None  # 4-tuple of 3-tuples

        self.camera_pos = None

        self.uv_N = None # unit vector N
        self.uv_V = None # unit vector V
        self.uv_U = None # unit vector U

        self.to_view_space = None
        self.to_screen_space = None

    def build_camera(self, elevation_angle, rotation_angle, radial_distance):
        # assume these are all given in degrees and must be converted to radians
        self.elevation_angle = radians(float(elevation_angle)) 
        self.rotation_angle = radians(float(rotation_angle))
        self.radial_distance = float(radial_distance) # not an angle

        self.camera_pos = (
            radial_distance * cos(elevation_angle) * cos(rotation_angle),
            radial_distance * cos(elevation_angle) * sin(rotation_angle),
            radial_distance * sin(elevation_angle)
        )

        # build vector CO
        v_CO = (
            0 - self.camera_pos[0],
            0 - self.camera_pos[1], 
            0 - self.camera_pos[2]
        ) # invert this if line is polar opposite direction
        magnitude = sqrt(v_CO[0]*v_CO[0] + v_CO[1]*v_CO[1] + v_CO[2]*v_CO[2]) # get the magnitude / norm
        # build unit vectors for new basis
        self.uv_N = (v_CO[0] / magnitude, v_CO[1] / magnitude, v_CO[2] / magnitude) # unit vector N
        self.uv_V = cross_product( self.uv_N, (0,0,1) ) # unit vector V
        self.uv_U = cross_product( self.uv_N, self.uv_V )    # unit vector U

        self.to_view_space = TransformationFactory.basis_change(self.uv_U, self.uv_V, self.uv_N, self.camera_pos) 
        print("world_to_camera:")
        print(self.to_view_space)
 

    def build_view_volume(self, near_plane, far_plane, width):
        self.d = near_plane
        self.f = far_plane
        self.h = width

        self.near_plane = (
           ( self.h, -self.h, self.d), 
           ( self.h,  self.h, self.d), 
           (-self.h,  self.h, self.d),
           (-self.h, -self.h, self.d)
        )

        slope = float(self.h) / float(self.d)
        h_at_f = slope * self.f

        self.far_plane = (
           ( h_at_f, -h_at_f, self.f), 
           ( h_at_f,  h_at_f, self.f), 
           (-h_at_f,  h_at_f, self.f),
           (-h_at_f, -h_at_f, self.f)
        )
        self.to_screen_space = TransformationFactory.to_screen_space(float(self.d), float(self.h), float(self.f))

    def render_scene(self, dimensions, image_name):
        to_canvas = TransformationFactory.to_canvas(dimensions)

        randy = Renderer(dimensions) # initialize renderer 

        print("Rendering...")

        # TO VIEW SPACE
        scene_edges = []
        scene_faces = []
        for model in self.scene.models:
            for face in model.faces:
                scene_faces.append(Face(face.v1, face.v2, face.v3, random_color()))
        print("faces in scene: {}".format(len(scene_faces)))
                
        scene_faces = transform_faces(scene_faces, self.to_view_space)
        print("basis swap to camera complete")

        # TODO: RENDER HERE
        self.render_face_edges(scene_faces, dimensions, image_name + "_beforeCulling", [self.to_screen_space, to_canvas])

        # TODO: CULLING

        before_filter = len(scene_faces)
        # scene_faces = list(filter(lambda face: face.should_cull(self.camera_pos), scene_faces))
        culled_faces = []
        for face in scene_faces:
            if not face.should_cull():
                culled_faces.append(face)

        difference = before_filter - len(culled_faces)
        print(str(difference) + " FACES CULLED")

        # TODO: RENDER HERE
        self.render_face_edges(culled_faces, dimensions, image_name + "_afterCulling", [self.to_screen_space, to_canvas])



        return

        # TO SCREEN SPACE
        solution_dict = {}
        for index in range(0, len(scene_edges)):
            first = scene_edges[index][0]
            second = scene_edges[index][1]

            p0 = solution_dict.get(first)
            p1 = solution_dict.get(second)

            if p0 == None:
                p0 = apply_transformation(first, self.to_screen_space)
                solution_dict[first] = p0
            
            if p1 == None:
                p1 = apply_transformation(second, self.to_screen_space)
                solution_dict[second] = p1

        # TODO: Clipping

        # TODO: RENDER HERE

        # TODO: Rasterize

        # TODO: Z-Buffer

        

        solution_dict = {}
        for index in range(0, len(scene_edges)):
            first = scene_edges[index][0]
            second = scene_edges[index][1]

            p0 = solution_dict.get(first)
            p1 = solution_dict.get(second)

            if p0 == None:
                p0 = apply_transformation(first, write_to_canvas)
                solution_dict[first] = p0
            
            if p1 == None:
                p1 = apply_transformation(second, write_to_canvas)
                solution_dict[second] = p1

            if (p0[2] >= 0 and p0[2] <= 1) or (p1[2] >= 0 and p1[2] <= 1):
                randy.drawLine(p0[0], p0[1], p1[0], p1[1]) # draw line

        # TODO: RENDER HERE
        randy.save(image_name) # create, write, and save image file

        print("image saved!")

    def render_edges(self, scene_edges, dimensions, image_name, transformations):
        randy = Renderer(dimensions)

        scene_edges = transform_edges(scene_edges, transformations[0])
        scene_edges = transform_edges(scene_edges, transformations[1])
        
        for edge in scene_edges:
            p0 = edge[0]
            p1 = edge[1]

            # p0 = solution_dict.get(first)
            # p1 = solution_dict.get(second)

            # if p0 == None:
            #     p0 = first
            #     for t in transformations:
            #         p0 = apply_transformation(p0, t)
            #     solution_dict[first] = p0
            
            # if p1 == None:
            #     p1 = second 
            #     for t in transformations:
            #         p1 = apply_transformation(p1, t)
            #     solution_dict[second] = p1

            randy.drawLine(p0[0], p0[1], p1[0], p1[1]) # draw line

        # TODO: RENDER HERE
        randy.save(image_name) # create, write, and save image file

    def render_face_edges(self, scene_faces, dimensions, image_name, transformations):
        randy = Renderer(dimensions)

        # print("VIEW SPACE: ", scene_faces[0].get_edges())
        # scene_faces = transform_faces(scene_faces, transformations[0])
        # print("SCREEN SPACE: ", scene_faces[0].get_edges())
        # scene_faces = transform_faces(scene_faces, transformations[1])
        # print("CANVAS SPACE: ", scene_faces[0].get_edges())

        scene_edges = []

        for face in scene_faces:
            for edge in face.get_edges():
                scene_edges.append(edge)
        
        print("edges collected!")
        print("# edges: {}".format(len(scene_edges)))

        scene_edges = transform_edges(scene_edges, transformations[0])
        scene_edges = transform_edges(scene_edges, transformations[1])
        
        for edge in scene_edges:
            p0 = edge[0]
            p1 = edge[1]

            # p0 = solution_dict.get(first)
            # p1 = solution_dict.get(second)

            # if p0 == None:
            #     p0 = first
            #     for t in transformations:
            #         p0 = apply_transformation(p0, t)
            #     solution_dict[first] = p0
            
            # if p1 == None:
            #     p1 = second 
            #     for t in transformations:
            #         p1 = apply_transformation(p1, t)
            #     solution_dict[second] = p1

            randy.drawLine(p0[0], p0[1], p1[0], p1[1]) # draw line
          


        # TODO: RENDER HERE
        randy.save(image_name) # create, write, and save image file

    
    