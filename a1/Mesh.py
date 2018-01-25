

class Mesh:

    def __init__(self):
        self.vertices = []
        self.edges = []

    def render(self):
        dimensions = 512

        if len(self.edges) > 0 and len(self.vertices) > 0:

            for edge in self.edges:

    