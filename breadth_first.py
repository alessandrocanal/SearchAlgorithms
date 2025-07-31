def breadth_first_search(graph, start, goal):
    frontier = [start]
    visited = set()

    while frontier:
        current = frontier.pop(0)

        if current == goal:
            break

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                frontier.append(neighbor)

    return len(visited)


# graph is a tree
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F','G']
}


path = breadth_first_search(graph, start='A', goal='D')
print("Breadth-First Path:", path)
