# 1. Add a check that the shortest path was found for each vertex
# 2. Print the shortest path from the source vertex to the target vertex

from collections import defaultdict

# Setting input values
input_list = [[1,2,1], [1,7,9], [2,3,2],[3,4,1], [4,7,2], [4,5,2], [5,6,1], [6,7,1], [7,9,6], [7,9,1], [7,8,2], [8,9,2]]
number_of_elements = 9
source = 1
target = 9

# Initializing the graph
graph = defaultdict(list)
# Fill in the graph: vertex - > (cost, vertex where we can go)
for a, b, cost in input_list:
    graph[a] += [(cost, b)]

# Initializing the list of vertexes to visit
nodes_to_visit = []
# Adding our original one with a distance equal to zero
nodes_to_visit.append((0, source))
# Initializing a list of unique values for storing vertexes that have already been visited
visited = set()
# Fill in the distance to all other vertexes
min_dist = {i: float('inf') for i in range(1, number_of_elements + 1)}
# Filling in the distance to the current vertex
min_dist[source] = 0
# We go through all the peaks that need to be visited
# Go through as long as there are such vertexes

while len(nodes_to_visit):
    # Take the closest peak to us
    # cost - hit cost, node-vertex name
    cost, node = min(nodes_to_visit)
    # Removing this vertex from the list of vertexes to visit
    nodes_to_visit.remove((cost, node))
    # We check that we haven't entered it yet (if we added (9,7) first and then (6,7)
    if node in visited:
        continue
    # Adding to the visited list
    visited.add(node)
    # We go through all connected vertexes
    # n_cost - the cost of getting from the current vertex
    # n_node - the attached vertex that we want to get to
    for n_cost, n_node in graph[node]:
        # Check if we found the optimal path
        if cost + n_cost < min_dist[n_node] and n_node not in visited:
            # If found, we update the distance value
            min_dist[n_node] = cost + n_cost
            # And add this vertex to the list of vertices to visit
            nodes_to_visit.append((cost + n_cost, n_node))

#1
if len(visited) == number_of_elements:
    print(min_dist[target])
else:
    print("We can't find the shortest path for all vertexes")

#2
path= []
s = source
t = target
while t != s:
    for i in input_list:
        if i[1] == t:
            if min_dist[t] - i[2] ==min_dist[i[0]]:
                path.insert(0, i[0])
                t = i[0]
                break
print(path)