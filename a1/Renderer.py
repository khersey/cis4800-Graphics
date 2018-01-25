from Mesh import *
from math import *

class Renderer:

    def __init__(self, mesh, dimensions):
        self.mesh = mesh
        self.dimensions = dimensions
        self.canvas = []
        for i in range(0, dimensions):
            row = []
            for j in range(0, dimensions):
                row.append( (0,0,0) )
            self.canvas.append(row)

    def render(self):
        offset = self.dimensions / 2

        for edge in self.mesh.edges:
            x0 = (edge[0][0] + 1) * offset
            y0 = (edge[0][1] + 1) * offset
            x1 = (edge[1][0] + 1) * offset
            y1 = (edge[1][1] + 1) * offset

            drawLine(x0, y0, x1, y1)

    def plot(self, x, y, c):
        # do actual draw here

    def ipart(self, x):
        return floor(float(x))

    def round(self, x):
        return self.ipart(float(x) + 0.5)

    def fpart(self, x):
        return float(x) - floor(x)

    def rfpart(self, x):
        return 1 - self.fpart(x)

    def drawLine(x0, y0, x1, y1):
        steep = abs(y1-y0) > abs(x1 - x0)

        if steep:
            y0, x0 = x0, y0
            y1, x1 = x1, y1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dx = x1 - x0
        dy = y1 - y0
        gradient = float(dy) / float(dx)
        if dx == 0:
            gradient = 1.0

        # first endpoint
        xend = self.round(x0)
        yend = float(y0) + gradient * (xend - float(x0))
        xgap = self.rfpart(float(x0) + 0.5)

        

        
