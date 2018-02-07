from math import *
from mathUtil import *

class ViewSystem:

    def __init__(self, elevation_angle, rotation_angle, radial_distance):
        # assume these are all given in degrees and must be converted to radians
        self.elevation_angle = radians(float(elevation_angle)) 
        self.rotation_angle = radians(float(rotation_angle))
        self.radial_distance = radial_distance # not an angle

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



        self.camera_pos = (
            radial_distance * cos(elevation_angle) * cos(rotation_angle),
            radial_distance * cos(elevation_angle) * sin(rotation_angle),
            radial_distance * sin(elevation_angle)
        )

        # this might move
        # build vector CO->
        v_CO = (
            0 - self.camera_pos[0],
            0 - self.camera_pos[1], 
            0 - self.camera_pos[2]
        ) # invert this if line is polar opposite direction
        magnitude = sqrt(v_CO[0]*v_CO[0] + v_CO[1]*v_CO[1] + v_CO[2]*v_CO[2]) # get the magnitude / norm
        # build unit vectors for new basis
        self.uv_N = (v_CO[0] / magnitude, v_CO[1] / magnitude, v_CO[2] / magnitude) # unit vector N
        self.uv_V = cross_product( uv_N, (0,1,0) ) # unit vector V
        self.uv_U = cross_product( uv_N, uv_V )    # unit vector U

        # do I define my view volume relative to my world frame or my view frame?

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
        h_at_f = slope * f

        self.far_plane = (
           ( h_at_f, -h_at_f, self.f), 
           ( h_at_f,  h_at_f, self.f), 
           (-h_at_f,  h_at_f, self.f),
           (-h_at_f, -h_at_f, self.f)
        )

        


    


