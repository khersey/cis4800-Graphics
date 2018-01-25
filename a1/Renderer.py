from Mesh import *
from math import *
from PIL import Image
from itertools import chain
import numpy as np

class Renderer:

    def __init__(self):
        self.mesh = None
        self.dimensions = 0
        self.canvas = None

    def render(self, mesh, dimensions, image_name):
        self.dimensions = dimensions
        self.mesh = mesh
        if not image_name.endswith(".jpg"):
            image_name = image_name + ".jpg"

        # prep canvas
        self.canvas = []
        for i in range(0, dimensions):
            row = []
            for j in range(0, dimensions):
                row.append( (0,0,0) )
            self.canvas.append(row)

        image = Image.new("RGB", (dimensions, dimensions), (0,0,0) )

        offset = self.dimensions / 2

        for edge in self.mesh.edges:
            x0 = (edge[0][0] + 1) * offset
            y0 = (edge[0][1] + 1) * offset
            x1 = (edge[1][0] + 1) * offset
            y1 = (edge[1][1] + 1) * offset

            self.drawLine(x0, y0, x1, y1)
        flat_canvas = list(chain.from_iterable(self.canvas))
        image.putdata(flat_canvas)
        
        image.save(image_name, "JPEG")
        image.close()
        

    def plot(self, x, y, c):
        # do actual draw here
        px = int(x)
        py = int(y)
        cc = int( 255.0 * c )

        if px >= self.dimensions:
            px = self.dimensions - 1
        if py >= self.dimensions:
            py = self.dimensions - 1

        # maybe only draw if cc is greater than pixels current value
        self.canvas[px][py] = (cc, cc, cc)

    def ipart(self, x):
        return floor(x)

    def round(self, x):
        return self.ipart(x + 0.5)

    def fpart(self, x):
        return x - floor(x)

    def rfpart(self, x):
        return 1 - self.fpart(x)

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
            gradient = dy / dx

        # first endpoint
        xend = self.round(x0)
        yend = y0 + gradient * (xend - x0)
        xgap = self.rfpart(x0 + 0.5)
        xpx11 = int(xend)
        ypx11 = int(self.ipart(yend)) 
        if steep:
            self.plot(ypx11, xpx11, self.rfpart(yend) * xgap)
            self.plot(ypx11 + 1, xpx11, self.fpart(yend) * xgap)
        else:
            self.plot(xpx11, ypx11, self.rfpart(yend) * xgap)
            self.plot(xpx11 , ypx11 + 1, self.fpart(yend) * xgap)
        intery = yend + gradient

        # second endpoint
        xend = self.round(x1)
        yend = y1 + gradient * (xend - x1)
        xgap = self.rfpart(x1 + 0.5)
        xpx12 = int(xend)
        ypx12 = int(self.ipart(yend)) 
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
                self.plot(self.ipart(intery) + 1, x, self.rfpart(intery))
                intery = intery + gradient
        else:
            for x in range(xpx11 + 1, xpx12 - 1):
                self.plot(x, self.ipart(intery), self.rfpart(intery))
                self.plot(x, self.ipart(intery) + 1, self.rfpart(intery))
                intery = intery + gradient

        

        
