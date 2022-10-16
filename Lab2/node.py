from copy import deepcopy
from mahattan import manhattan_distance

class Node:
    def __init__(self, parent, state, move, depth, goal, h2):
        self.parent = parent
        self.state = state
        self.move = move
        self.goal = goal
        if parent:
            self.depth = parent.depth + depth
        else:
            self.depth = depth
        self.h2 = h2
        if h2:
            self.eval_func = manhattan_distance(state, goal) + self.depth

    def expand(self):
        children = []
        for i, row in enumerate(self.state):
            for j, num in enumerate(row):
                if num == 0:
                    pos = (i, j)
        moves = []
        if pos[0] != 0:
            moves.append('down')
        if pos[0] != 2:
            moves.append('up')
        if pos[1] != 0:
            moves.append('right')
        if pos[1] != 2:
            moves.append('left')

        for move in moves:
            new_state = deepcopy(self.state)
            if move == 'down':
                new_state[pos[0]][pos[1]], new_state[pos[0]-1][pos[1]] = new_state[pos[0]-1][pos[1]], new_state[pos[0]][pos[1]]
            elif move == 'up':
                new_state[pos[0]][pos[1]], new_state[pos[0]+1][pos[1]] = new_state[pos[0]+1][pos[1]], new_state[pos[0]][pos[1]]
            elif move == 'right':
                new_state[pos[0]][pos[1]], new_state[pos[0]][pos[1]-1] = new_state[pos[0]][pos[1]-1], new_state[pos[0]][pos[1]]
            elif move == 'left':
                new_state[pos[0]][pos[1]], new_state[pos[0]][pos[1]+1] = new_state[pos[0]][pos[1]+1], new_state[pos[0]][pos[1]]
            children.append(Node(self, new_state, move, 1, self.goal, self.h2))
        return children