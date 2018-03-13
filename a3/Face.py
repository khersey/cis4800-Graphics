import mathUtil

class Face:

    def __init__(self, vertex1, vertex2, vertex3, color = (255, 255, 255)):
        self.v1 = vertex1
        self.v2 = vertex2
        self.v3 = vertex3
        self.nN = self.generate_normal()
        self.rgb = color
        
    # returns list of edges
    def get_edges(self):
        edges = []
        edges.append( (self.v1, self.v2) )
        edges.append( (self.v2, self.v3) )
        edges.append( (self.v3, self.v1) )
        return edges

    def get_vertices(self):
        return [self.v1, self.v2, self.v3]

    # return boolean
    def should_cull(self):        
        cp = mathUtil.vector_from_points(self.v1, (0,0,0))
        result = mathUtil.dot_product(cp, self.nN)

        print("cp = {}".format(self.v1))
        print("nN = {}".format(self.nN))
        print("cp . Nn = {}".format(result))
        return result >= 0

    def generate_normal(self):
        vectorU = mathUtil.vector_from_points(self.v1, self.v2)
        vectorV = mathUtil.vector_from_points(self.v1, self.v3)
        self.nN = mathUtil.cross_product(vectorU, vectorV)


