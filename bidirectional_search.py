# deque is better than a simple list because the method popleft() is O(1) meanwhile pop(0) is O(n)
from collections import deque

#defaultdict works just like a regular dict, but with a default value for missing keys. It automatically creates a value when you try to access a key that doesn’t exist
from collections import defaultdict

def make_undirected(graph):
    new_graph = defaultdict(list)
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            new_graph[node].append(neighbor)
            new_graph[neighbor].append(node)  # Add reverse edge
    return dict(new_graph)


def rebuild_path(came_from_start, came_from_goal, neighbor):
    path = [neighbor]
    node = came_from_start[neighbor]
    while node:
        path.append(node)
        node = came_from_start[node]
    path.reverse()
    node = came_from_goal[neighbor]
    while node:
        path.append(node)
        node = came_from_goal[node]

    return path


def bidirectional_search(given_graph, start, goal):
    graph = make_undirected(given_graph)

    frontier_start = deque([start])
    frontier_goal = deque([goal])

    visited_start = {start}
    visited_goal = {goal}

    came_from_start = {start: None}
    came_from_goal = {goal: None}

    while frontier_start and frontier_goal:
        current_start = frontier_start.popleft()
        for neighbor in graph[current_start]:
            if neighbor not in visited_start:
                came_from_start[neighbor] = current_start
                frontier_start.append(neighbor)
                visited_start.add(neighbor)
            if neighbor in visited_goal:
                # MEETING POINT FOUND!
                # we must rebuild the path
                return rebuild_path(came_from_start, came_from_goal, neighbor)
        current_goal = frontier_goal.popleft()
        for neighbor in graph[current_goal]:
            if neighbor not in visited_goal:
                came_from_goal[neighbor] = current_goal
                frontier_goal.append(neighbor)
                visited_goal.add(neighbor)
            if neighbor in visited_start:
                # MEETING POINT FOUND!
                # we must rebuild the path
                return rebuild_path(came_from_start, came_from_goal, neighbor)


graph = {
    'A': ['B','F'],
    'B': ['C','G'],
    'G': ['K'],
    'K': ['M']
}


path = bidirectional_search(graph, start='A', goal='M')
print(path)
