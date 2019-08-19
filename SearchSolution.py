#Outline provided
#No Code Additions - Himadri Narasimhamurthy
#CS76 - 19W - M&C


class SearchSolution:
    def __init__(self, problem, search_method, safe_boat):
        self.problem_name = str(problem)
        self.search_method = str(search_method)
        self.path = []
        self.nodes_visited = 0
        self.safe_boat = safe_boat

    def setpath(self, path):
        self.path = path

    def __str__(self):
        string = "----\n"
        string += "{:s}\n"
        if not self.safe_boat:
            string += "attempted with search method {:s} and strict rules - the boat was NOT a safe zone\n"
        else:
            string += "attempted with search method {:s} and the boat WAS a safe zone - a cannibal in the boat couldn't eat those off the boat\n"

        if len(self.path) > 0:

            string += "number of nodes visited: {:d}\n"
            string += "solution length: {:d}\n"
            string += "path: {:s}\n"

            string = string.format(self.problem_name, self.search_method,
                self.nodes_visited, len(self.path), str(self.path))
        else:
            string += "no solution found after visiting {:d} nodes\n"
            string = string.format(self.problem_name, self.search_method, self.nodes_visited)

        return string
