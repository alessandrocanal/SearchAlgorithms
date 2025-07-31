import heapq

def best_first_search(graph, heuristic, start, goal):
    frontier = []
    heapq.heappush(frontier, (heuristic[start], start))
    came_from = {start: None}
    visited = set()

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        visited.add(current)

        for neighbor, distance in graph[current]:
            if neighbor not in visited and neighbor not in came_from:
                came_from[neighbor] = current
                heapq.heappush(frontier, (heuristic[neighbor], neighbor))

    # Reconstruct path
    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from.get(node)
    path.reverse()

    return path


# Graph: adjacency list with (neighbor, cost)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': [('E', 1)],
    'E': []
}

# Heuristic: estimated cost to goal (E)
heuristic = {
    'A': 4,
    'B': 2,
    'C': 2,
    'D': 1,
    'E': 0
}

path = best_first_search(graph, heuristic, start='A', goal='E')
print("Best-First Path:", path)
