import heapq

def dijkstra_search(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    all_nodes = set(graph.keys())
    for edges in graph.values():
        for neighbor, _ in edges:
            all_nodes.add(neighbor)

    # Correct distance initialization
    distance_cost = {node: float('inf') for node in all_nodes}
    distance_cost[start] = 0

    while frontier:
        cost,current = heapq.heappop(frontier)

        if current == goal:
            break

        for neighbor, distance in graph[current]:
            new_cost = distance + cost
            if new_cost < distance_cost[neighbor]:
                distance_cost[neighbor] = new_cost
                came_from[neighbor] = current
                heapq.heappush(frontier, (new_cost, neighbor))

    path = [goal]
    if goal in came_from.keys():
        source = came_from[goal]
        path.append(source)
        while source != start:
            source = came_from[source]
            path.append(source)
        path.reverse()
        return path
    else:
        return []



graph = {
    'Sibiu': [('Rimicu Vilcea',80),('Fagaras',99)],
    'Fagaras': [('Bucharest',101)],
    'Rimicu Vilcea': [('Pitesti',97)],
    'Pitesti': [('Bucharest',201)]
}

path = dijkstra_search(graph, 'Sibiu', 'Bucharest')
print(path)