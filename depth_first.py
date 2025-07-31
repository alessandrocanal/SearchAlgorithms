def depth_first_search(graph, start, goal):
    frontier = [start]
    came_from = {start: None}
    reached = False

    while frontier:
        current = frontier.pop()

        if current == goal:
            reached = True
            break

        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in came_from:
                    frontier.append(neighbor)
                    came_from[neighbor] = current

    path = []
    if reached:
        node = goal
        while node:
            path.append(node)
            node = came_from.get(node)
        path.reverse()

    return path



# graph is a tree, so this is a suitable case for this algorithm: no infinite loops
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['O', 'P']
}


path = depth_first_search(graph, 'A', 'M')
print(path)