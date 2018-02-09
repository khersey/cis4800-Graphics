from math import *

from mathUtil import *
from Renderer import *
from Mesh import *
from Scene import *

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

        self.world_to_camera = None
        self.project_to_window = None

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

        self.world_to_camera = TransformationFactory.basis_change(self.uv_U, self.uv_V, self.uv_N, self.camera_pos) 
        print("world_to_camera:")
        print(self.world_to_camera)
 

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

        self.project_to_window = TransformationFactory.view_plane_projection(float(self.d))

    def edge_in_view_volume(self, edge):
        q = self.h/self.d
        for p in edge:
            if p[0] < -q*p[2] or p[0] > q*p[2] or p[1] < -q*p[2] or p[1] > q*p[2] or p[2] > self.f or p[2] < self.d:
                return False
        return True



    def render_scene(self, dimensions, image_name):

        randy = Renderer(dimensions) # initialize renderer 

        print("Rendering...")

        # move everything to camera basis
        solution_dict = {}
        scene_edges = []
        for model in self.scene.models:
            for edge in model.edges:
                first = edge[0]
                second = edge[1]

                new_first = solution_dict.get(first)
                new_second = solution_dict.get(second)

                if new_first == None:
                    new_first = apply_transformation(first, self.world_to_camera)
                    solution_dict[first] = new_first
                
                if new_second == None:
                    new_second = apply_transformation(second, self.world_to_camera)
                    solution_dict[second] = new_second
                
                # print("old: " + str(edge))
                # print("new: " + str((new_first, new_second)))
                scene_edges.append( (new_first, new_second) )
        print("basis swap to camera complete")


        before_filter = len(scene_edges)
        scene_edges = list(filter(self.edge_in_view_volume, scene_edges))
        difference = before_filter - len(scene_edges)
        print(str(difference) + " edges removes from outside of view volume")

        # project to window and write to canvas
        write_to_canvas = TransformationFactory.scale_to_image(float(dimensions), float(self.h), float(self.d))
        write_to_canvas = matrix_multiplication(write_to_canvas, self.project_to_window)

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

            randy.drawLine(p0[0], p0[1], p1[0], p1[1]) # draw line

        randy.save(image_name) # create, write, and save image file

        print("image saved!")

        
    

    