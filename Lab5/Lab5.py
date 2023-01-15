import random

class graph:
    def __init__(self, n, weights, edges):
        self.size = n
        self.grph = {}
        for i in range(1, n+1):
            self.grph[i] = [[],[]]
        for i in range(1, n+1):
            if len(self.grph[i][1]) < edges:
                extent = random.randint(1,edges - len(self.grph[i][1]))
                while len(self.grph[i][1]) < extent and len(self.grph[i][1]) < edges:
                    j = random.randint(1,n)
                    while j == i and j not in self.grph[i][1] and len(self.grph[j][1]) < edges:
                        j = random.randint(1,n)
                    weight = random.randint(weights[0],weights[1])
                    self.grph[i][1].append(j)
                    self.grph[j][1].append(i)
                    self.grph[i][0].append(weight)
                    self.grph[j][0].append(weight)
        self.savegraph()

    def DFS(self, start, end):
        visited = []
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                edges = self.grph[node][1]
                for edge in edges:
                    newpath = path[:]
                    newpath.append(edge)
                    queue.append(newpath)
                    if edge == end:
                        return self.getpathwieght(newpath)
                visited.append(node)
        return None

    def savegraph(self):
        visited = set([])
        with open('./Lab5/graph.txt', 'w') as f:
            for node, info in self.grph.items():
                for i in range(len(info[0])):
                    if f'{node}-{info[1][i]}' not in visited and f'{info[1][i]}-{node}' not in visited:
                        print(f'Edge: {node}-{info[1][i]}; Weight: {info[0][i]}', file=f)
                        visited.add(f'{node}-{info[1][i]}')

    def getrandompath(self, start, end, exvisited = None):
        if not exvisited:
            visited = set([start])
        else:
            visited = set(exvisited[:])
        path = [start]
        currnode = path[-1]
        while end != currnode:
            edges = self.grph[path[-1]][1][:]
            for index, edge in enumerate(edges):
                if edge in visited:
                    edges.pop(index)
            if not edges or all(edge in visited for edge in edges):
                while all(edge in visited for edge in self.grph[path[-1]][1]) and len(path) > 1:
                    visited.add(path.pop(-1))
                if len(path) == 1 and all(edge in visited for edge in self.grph[path[0]][1]):
                    return None
            else:
                path.append(edges[random.randint(0,len(edges)-1)])
            currnode = path[-1]
            visited.add(currnode)
        return path

    def getpathwieght(self, path):
        weight = 0
        prevnode = path[0]
        for node in path[1:]:
            weight += self.grph[node][0][self.grph[node][1].index(prevnode)]
            prevnode = node
        return weight

    def improvepath(self, path):
        newpath = None
        while not newpath:
            pathchunk = path[:random.randint(1,len(path)-2)]
            newpath = self.getrandompath(pathchunk[-1], path[-1], pathchunk)
            if newpath:
                newpath = pathchunk + newpath[1:]
        return newpath

    def pathexists(self, start, end):
        visited = set([start])
        edgeid = 0
        while end not in visited and edgeid < len(visited):
            for edge in self.grph[list(visited)[edgeid]][1]:
                visited.add(edge)
            edgeid += 1
        if end not in visited:
            return False
        else:
            return True

class ABC:
    def __init__(self, scouts, workers, iterationlimit):
        self.scoutsamount = scouts
        self.workersamount = workers
        self.iterationlimit = iterationlimit
        self.scoutedpaths = []
        self.bestpath = None

    def solve(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        if not graph.pathexists(start, end) or start == end:
            return None
        dfsresult = self.graph.DFS(start, end)
        foundbetterpath = False 
        iteration = 0
        while not foundbetterpath and iteration < self.iterationlimit:
            self.Scout()
            self.Sortpaths()
            self.Worker()
            self.SaveBest()
            if self.bestpath[1] < dfsresult:
                foundbetterpath = True
            iteration += 1
        return dfsresult, self.bestpath

    def Sortpaths(self):
        self.pathsprobability = []
        if len(self.scoutedpaths) > 1:
            wsum = 0
            for _, weight in self.scoutedpaths:
                wsum += weight
            prob = 0
            for path, weight in self.scoutedpaths:
                prob += 1 - weight / wsum
                self.pathsprobability.append((path, weight, prob))
        else:
            self.pathsprobability.append((self.scoutedpaths[0][0], self.scoutedpaths[0][1], 1))

    def Scout(self):
        self.scouts = []
        self.scoutedpaths = []
        scoutsrange = self.scoutsamount if self.scoutsamount <= self.graph.size else self.graph.size
        for i in range(scoutsrange):
            path = self.graph.getrandompath(self.start, self.end)
            self.scouts.append((path, self.graph.getpathwieght(path)))
            self.scoutedpaths.append(self.scouts[i])

    def Worker(self):
        self.workers = []
        for i in range(self.workersamount):
            prob = random.uniform(0,1)
            j = 0
            while len(self.pathsprobability) != j+1:
                if self.pathsprobability[j+1][2] > prob >= self.pathsprobability[j][2]:
                    self.workers.append((self.pathsprobability[j+1][0], self.pathsprobability[j+1][1]))
                j += 1
            if len(self.workers) < i+1:
                self.workers.append((self.pathsprobability[0][0], self.pathsprobability[0][1]))
        for index, worker in enumerate(self.workers):
            if len(worker[0]) > 2:
                outskirtpath = self.graph.improvepath(worker[0])
                outskirtpathweight = self.graph.getpathwieght(outskirtpath)
                if outskirtpathweight < worker[1]:
                    self.workers[index] = (outskirtpath, outskirtpathweight)

    def SaveBest(self):
        for worker in self.workers:
            if not self.bestpath:
                self.bestpath = worker
            elif worker[1] < self.bestpath[1]:
                self.bestpath = worker

n = 300
weights = (5, 150)
maxedges = 10
grph = graph(n, weights, maxedges)
Workers = 90
Scouts = 10
iterationlimit = 100
start, end = [int(i) for i in input("Input start node and destination node in format \"a,b\" - ").split(",")]
sol = ABC(Scouts, Workers, iterationlimit)
result = sol.solve(grph, start, end)
while not result:
    start, end = [int(i) for i in input("Input valid start node and destination node in format \"a,b\" - ").split(",")]
    result = sol.solve(grph, start, end)
print(f"DFS weight = {result[0]}\nResult path - {' -> '.join([str(i) for i in result[1][0]])}\nPath weight = {result[1][1]}")