from Mesh import *
from math import *
from PIL import Image
from itertools import chain

class Renderer:

    def __init__(self, dimensions):
        self.dimensions = dimensions
        # prep canvas
        self.frame_buffer = []
        self.z_buffer = []
        self.reset()

    def reset(self):
        self.frame_buffer = []
        for i in range(0, self.dimensions):
            row = []
            for j in range(0, self.dimensions):
                row.append( (0,0,0) )
            self.frame_buffer.append(row)
        
        self.z_buffer = []
        for i in range(0, self.dimensions):
            row = []
            for j in range(0, self.dimensions):
                row.append(1)
            self.z_buffer.append(row)


    def save(self, image_name):
        flat_canvas = list(chain.from_iterable(self.frame_buffer))
        image = Image.new("RGB", (self.dimensions, self.dimensions), (0,0,0) )
        image.putdata(flat_canvas)
        image.save(image_name + ".jpg", "JPEG")
        image.close()
        print("RANDY: I've rendered " + image_name + ".jpg for your health")
        self.reset()


    def rasterize(self, face):
        # pre compute dictionary size
        y_vals = [ self.round(face.v1[1]), self.round(face.v2[1]), self.round(face.v3[1]) ]
 
        y_min = min(y_vals)
        y_max = max(y_vals)

        # format:
        # row_dict[y] = [(x0, z0), (x1, z1)]
        row_dict = {}
        # figure out what y values will be used (not including y-max), dict[y] = []
        for y in range(y_min, y_max):
            row_dict[y] = []

        # go through lines set dict[y] = [xstart, xmax]
        for edge in face.get_edges():
            if self.round(edge[0][1]) != self.round(edge[1][1]):
                line = self.rasterize_line(edge)
                # print(line)
                for pixel in line:
                    x, y, z = pixel[0], pixel[1], pixel[2]
                    if y != y_max:
                        if row_dict.get(y) == None:
                            print(face.get_edges())
                            print(line)
                        row = row_dict[y]
                        # print("row[{}] = ({}, {})".format(y, x, z))
                        row.append( (x, z) )
                        row_dict[y] = row

        xs, xe, zs, ze = 0, 0, 0.0, 0.0
        for y in range(y_min, y_max):
            row = row_dict[y]
            # print("row[{}] = {}".format(y, row))

            if row[0][0] > row[1][0]:
                xs, xe = row[1][0], row[0][0]
                zs, ze = row[1][1], row[0][1]
            else:
                xs, xe = row[0][0], row[1][0]
                zs, ze = row[0][1], row[1][1]

            z = zs
            z_delta = 0.0
            if xe - xs != 0:
                z_delta = (ze - zs) / (xe - xs)

            for x in range(xs, xe):
                if z < self.z_buffer[y][x]:
                    self.z_buffer[y][x] = z
                    self.frame_buffer[y][x] = face.rgb
                z += z_delta


    def rasterize_line(self, edge):
        line = []
        # convert x and y to ints
        x0 = self.round(edge[0][0])
        y0 = self.round(edge[0][1])
        z0 = edge[0][2]
        x1 = self.round(edge[1][0])
        y1 = self.round(edge[1][1])
        z1 = edge[1][2]

        if y0 > y1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
            z0, z1 = z1, z0

        delta_z = (z1 - z0) / (y1 - y0)

        z = z0
        x = x0
        m = (x1 - x0) / (y1 - y0)
        for y in range(y0, y1 + 1):
            line.append((self.round(x), y, z))
            x += m
            # increment our values
            z += delta_z

        return line

    def plot(self, x, y, c):
        # do actual draw here
        px = int(x)
        py = int(y)
        cc = int( 255.0 * c )

        if (px < self.dimensions and py < self.dimensions and px >= 0 and py >= 0):
            self.frame_buffer[py][px] = (cc, cc, cc)


    def ipart(self, x):
        return floor(x)

    def round(self, x):
        return self.ipart(x + 0.5)

    def fpart(self, x):
        return x - floor(x)

    def rfpart(self, x):
        return 1.0 - self.fpart(x)

    def drawLine(self, x0, y0, x1, y1):
        steep = abs(y1 - y0) > abs(x1 - x0)

        if steep:
            y0, x0 = x0, y0
            y1, x1 = x1, y1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dx = x1 - x0
        dy = y1 - y0
        
        if dx == 0:
            gradient = 1.0
        else: # must be nested to prevent division by 0 error
            gradient = float(dy) / float(dx)

        # first endpoint
        xend = self.round(x0)
        yend = float(y0) + gradient * (float(xend) - float(x0))
        xgap = self.rfpart(float(x0) + 0.5)
        xpx11 = int(xend)
        ypx11 = self.ipart(yend)
        if steep:
            self.plot(ypx11, xpx11, self.rfpart(yend) * xgap)
            self.plot(ypx11 + 1, xpx11, self.fpart(yend) * xgap)
        else:
            self.plot(xpx11, ypx11, self.rfpart(yend) * xgap)
            self.plot(xpx11, ypx11 + 1 , self.fpart(yend) * xgap)
        intery = float(yend + gradient)

        # second endpoint
        xend = self.round(float(x1))
        yend = y1 + gradient * (xend - x1)
        xgap = self.rfpart(float(x1) + 0.5)
        xpx12 = int(xend)
        ypx12 = self.ipart(yend)
        if steep:
            self.plot(ypx12, xpx12, self.rfpart(yend) * xgap)
            self.plot(ypx12 + 1, xpx12, self.fpart(yend) * xgap)
        else:
            self.plot(xpx12, ypx12, self.rfpart(yend) * xgap)
            self.plot(xpx12 , ypx12 + 1, self.fpart(yend) * xgap)

        # main loop -> draw that line
        if steep:
            for x in range(xpx11 + 1, xpx12 - 1):
                self.plot(self.ipart(intery), x, self.rfpart(intery))
                self.plot(self.ipart(intery) + 1, x, self.fpart(intery))
                intery = intery + gradient
        else:
            for x in range(xpx11 + 1, xpx12 - 1):
                self.plot(x, self.ipart(intery), self.rfpart(intery))
                self.plot(x, self.ipart(intery) + 1, self.fpart(intery))
                intery = intery + gradient

        

        
