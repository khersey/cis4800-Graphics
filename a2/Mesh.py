

class Mesh:

    def __init__(self):
        self.vertices = []
        self.edges = []
        self.queued_transformations = []
        self.applied_transformations = []

    def add_transformation(self, transformation):
        self.queued_transformations.append(transformation)
    
    def apply_transformations(self):
        solution_dict = {}

        # this is a problem best suited to a shader 

        # TODO: transform vertex array and save solutions, then apply solutions to vertices in edge array

        for edge_index in range(0, len(self.edges)):
            edge = self.edges[edge_index]
            # check if we have transformed this vertex previously
            final_first = solution_dict.get(edge[0]) # first vertex in the line
            final_second = solution_dict.get(edge[1])

            if final_first == None or final_second == None:
                first = list(edge[0]) 
                second = list(edge[1])
                first.append(1)
                second.append(1)

                for matrix in self.queued_transformations:
                    new_first =  [0.0, 0.0, 0.0, 0.0]
                    new_second = [0.0, 0.0, 0.0, 0.0]
                    for i in range(0,4):

                        if final_first == None:
                            for j in range(0,4):
                                new_first[i] += first[j] * matrix[i][j]

                        if final_second == None:
                            for j in range(0,4):
                                new_second[i] += second[j] * matrix[i][j]
                    # modify first and second for next iteration
                    first = new_first
                    second = new_second

                if final_first == None:
                    final_first = tuple(new_first[:3])
                    solution_dict[ edge[0] ] = final_first

                if final_second == None:
                    final_second = tuple(new_second[:3])
                    solution_dict[ edge[1] ] = final_second

            print("old: " + str(edge[0]) + ", " + str(edge[1]))
            print("new: " + str(final_first) + ", " + str(final_second))
            self.edges[edge_index] = (final_first, final_second)
                    
        self.applied_transformations = self.applied_transformations + self.queued_transformations
        self.queued_transformations = []
                



    