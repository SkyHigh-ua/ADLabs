from node import Node
from sys import maxsize

class RBFS:
    def __init__(self, start_state, goal_state):
        self.state = start_state
        self.goal = goal_state

    def solve(self):
        return self.RBFS_search(Node(None, self.state, None, 0, self.goal, True), f_limit=maxsize)[0]

    def RBFS_search(self, node, f_limit):
        successors=[]

        if node.state == self.goal:
            return node,None

        children=node.expand()
        if not len(children):
            return None, maxsize

        for child in children:
            successors.append((child.eval_func, len(children)-1, child))

        while len(successors):

            successors.sort(key=lambda x: x[0])

            best_node = successors[0][2]

            if best_node.eval_func > f_limit:
                return None, best_node.eval_func

            alt = successors[1][0]

            result, best_node.eval_func = self.RBFS_search(best_node, min(f_limit, alt))

            successors[0] = (best_node.eval_func, successors[0][1], best_node)

            if result:
                return result, None