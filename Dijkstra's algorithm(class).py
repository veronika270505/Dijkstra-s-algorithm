class Dijkstra:

    def __init__(self, vertices, graph):
        self.vertices = vertices  # ("1", "2", "3" ...)
        self.graph = graph  # {"1": {"2": 1}, "2": {"1": 3, "3": 5} ...}

    def route(self, start, end):
        unvisited = {n: float("inf") for n in self.vertices}
        unvisited[start] = 0  # set start vertex to 0
        visited = {}  # list of all visited nodes
        parents = {}  # predecessors
        while unvisited:
            min_vertex = min(unvisited, key=unvisited.get)  # get smallest distance
            for neighbour, _ in self.graph.get(min_vertex, {}).items():
                if neighbour in visited:
                    continue
                new_distance = unvisited[min_vertex] + self.graph[min_vertex].get(neighbour, float("inf"))
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    parents[neighbour] = min_vertex
            visited[min_vertex] = unvisited[min_vertex]
            unvisited.pop(min_vertex)
            if min_vertex == end:
                break
        return parents, visited

    @staticmethod 
    # just gets the passed arguments, without the implicit first argument, and its definition is immutable through inheritance
    # allows you not to import each function separately
    def path(parents, start, end):
        path = [end]
        while True:
            key = parents[path[0]]
            path.insert(0, key)
            if key == start:
                break
        return path
    
input_vertices = ('1', '2', '3', '4', '5', '6', '7')
input_graph = {
    '1': {'2': 5, '4': 3, '5': 12, '5': 5},
    '2': {'1': 5, '4': 1, '7': 2},
    '3': {'5': 2, '6': 19, '7': 2},
    '4': {'1': 3, '2': 1, '5': 1, '7': 1},
    '5': {'1': 12, '3': 2, '4': 1, '6': 3},
    '6': {'1': 5, '3': 19, '5': 3},
    '7': {'2': 2, '3': 2, '4': 1}
    }
start_vertex = '3'
end_vertex= '6'
dijkstra = Dijkstra(input_vertices, input_graph)
p, v = dijkstra.route(start_vertex, end_vertex)
print("The distance from %s to %s is: %.2f" % (start_vertex, end_vertex, v[end_vertex]))
s = dijkstra.path(p, start_vertex, end_vertex)
print("The path from %s to %s is: %s" % (start_vertex, end_vertex, " -> ".join(s)))