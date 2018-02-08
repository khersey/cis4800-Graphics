from Mesh import *
from math import *
from PIL import Image
from itertools import chain

class Renderer:

    def __init__(self, dimensions):
        self.dimensions = dimensions
        # prep canvas
        self.canvas = []
        for i in range(0, dimensions):
            row = []
            for j in range(0, dimensions):
                row.append( (0,0,0) )
            self.canvas.append(row)

    def save(self, image_name):
        flat_canvas = list(chain.from_iterable(self.canvas))
        image = Image.new("RGB", (self.dimensions, self.dimensions), (0,0,0) )
        image.putdata(flat_canvas)
        image.save(image_name, "JPEG")
        image.close()

    def plot(self, x, y, c):
        # do actual draw here
        px = int(x)
        py = int(y)
        cc = int( 255.0 * c )

        # NOTE: x and y are flipped here, otherwise the image prints sideways
        if (px < self.dimensions and py < self.dimensions and px >= 0 and py >= 0):
            self.canvas[py][px] = (cc, cc, cc)


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

        

        
