import mathUtil

class Face:

    def __init__(self, vertex1, vertex2, vertex3, color = (255, 255, 255)):
        self.v1 = vertex1
        self.v2 = vertex2
        self.v3 = vertex3
        self.rgb = color

    # returns list of edges
    def get_edges(self):
        edges = []
        edges.append( (self.v1, self.v2) )
        edges.append( (self.v2, self.v3) )
        edges.append( (self.v3, self.v1) )
        return edges

    # return boolean
    def should_cull(self, c):
        cp = mathUtil.vector_from_points(c, self.v1)
        vector1 = mathUtil.vector_from_points(self.v1, self.v2)
        vector2 = mathUtil.vector_from_points(self.v1, self.v3)
        n  = mathUtil.cross_product(vector1, vector2)
        return mathUtil.dot_product(cp, n) >= 0