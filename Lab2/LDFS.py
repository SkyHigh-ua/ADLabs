from node import Node

class LDFS:
    def __init__(self, state, goal, depth):
        self.state = state
        self.goal = goal
        self.depth = depth
        # self.visited = []

    # def isvisited(self, node):
    #     for vnode in self.visited:
    #         if vnode.state == node.state:
    #             return True
    #     return False

    def solve(self):
        return self.LDFS_search(Node(None, self.state, None, 0, self.goal, False), self.depth)
    
    def LDFS_search(self, node, depth):
        result = None
        if depth >=1:
            if node.state == self.goal:
                return node
            # self.visited.append(node)
            children = node.expand()
            for child in children:
                # if not self.isvisited(child):
                #     self.visited.append(child)
                result = self.LDFS_search(child, depth-1)
                if result:
                    return result