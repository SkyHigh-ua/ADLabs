def index(lst, num):
    for i, row in enumerate(lst):
        if num in row:
            return (i, row.index(num))

def manhattan_distance(state, goal):
    distance = 0
    for i, row in enumerate(state):
        for j, num in enumerate(row):
            row_value, col_value = i, j
            row_goal, col_goal = index(goal, num)
            distance += abs(row_value - row_goal) + abs(col_value - col_goal)
    return distance