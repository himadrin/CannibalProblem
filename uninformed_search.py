#Outline provided
#Code Additions - Himadri Narasimhamurthy
#CS76 - 19W - M&C

from collections import deque
from SearchSolution import SearchSolution
from CannibalProblem import *

# you might find a SearchNode class useful to wrap state objects,
#  keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        # you write this part
        self.state = state
        self.parent = parent

def bfs_search(search_problem, safe_boat):
    start = search_problem.start_state

    #dictionary of backpointers - we initialize start with none
    back_dict = {}
    back_dict[start] = None

    q = deque()
    q.append(start)

    #remove nodes from the queue until we get to end
    while q:
        node = q.popleft()
        successors = search_problem.get_successors(node, safe_boat)

        #go through each of the neighbors
        for vert in successors:
            if vert not in back_dict:
                back_dict[vert] = node
                #add new vertices to the structures
                q.append(vert)

                if search_problem.goal_test(vert):
                    sol = SearchSolution(search_problem, "BFS", safe_boat)
                    sol.path = backchain(back_dict, vert)
                    sol.nodes_visited = len(back_dict)
                    return sol

    sol = SearchSolution(search_problem, "DFS", safe_boat)
    sol.nodes_visited = len(back_dict)
    return sol

#function to backchain - bfs to get the final path
def backchain(dict, i):
    path = []

    while i != None:
        path.insert(0,i)
        i = dict[i]
    return path

#recursive path checking dfs
def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    # if no node object given, create a new search from starting state
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS", True)

    #add visited node every time we recurse
    solution.nodes_visited = solution.nodes_visited + 1
    path = get_path(node)

    #return path if you find goal
    if search_problem.goal_test(node.state):
        solution.path = path
        return solution

    #if we recurse to limit, we return path
    elif len(path)>depth_limit:
        solution.path = path
        return solution

    #heres the recursion part - we go through all the successors
    for n in search_problem.get_successors(node.state, True):
        newNode = SearchNode(n, node)

        if newNode.state not in path:
            p = dfs_search(search_problem, depth_limit, newNode, solution)
            #if a path exists we return it
            if p.path:
                return p

    return solution

#this is the path checking function through the nodes which link back to parent
def get_path(n):
    backpath = []
    backpath.append(n.state)

    while n.parent != None:
        backpath.append(n.parent.state)
        n = n.parent

    return backpath


    # you write this part
def ids_search(search_problem, depth_limit=100):
    #create visited nodes variable for counting
    v = 0

    #call dfs within the depth range
    for depth in range(depth_limit):
        solution = dfs_search(search_problem, depth)
        v = v + 1
        #increment nodes visited

    if solution.path != None:
        solution.search_method = "IDS"
        solution.nodes_visited = v
        return solution
