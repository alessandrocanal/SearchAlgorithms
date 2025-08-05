import heapq
import copy

# first heuristic function
def hamming_distance(state,final_state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != final_state[i][j]:
                count += 1
    return count

# second heuristic function
def manhattan_distance(state, final_state):
    # to avoid O(n^4) I can define a dictionary with the goal positions
    goal_positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1)
        # 0 (blank) is optional — you usually ignore it
    }
    total = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                total += abs(i - goal_positions[state[i][j]][0]) + abs(j - goal_positions[state[i][j]][1])
    return total

def get_blank_position(state):
    for i, row in enumerate(state):
        for j, val in enumerate(row):
            if val == 0:
                return (i, j)

def get_neighbors(state):
    # Find 0
    zero_place = get_blank_position(state)

    # Generate possible new states (as copies)
    MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    moves_offset_list = []
    for dx,dy in MOVES:
        if 0 <= (zero_place[0] + dx) < 3 and 0 <= (zero_place[1] + dy) < 3:
            moves_offset_list.append((dx,dy))

    # Return list of valid states
    neighbors = []
    for dx,dy in moves_offset_list:
        new_state = copy.deepcopy(state)
        x = zero_place[0] + dx
        y = zero_place[1] + dy

        new_state[x][y], new_state[zero_place[0]][zero_place[1]] = new_state[zero_place[0]][zero_place[1]], new_state[x][y]

        neighbors.append(new_state)
    return neighbors

def eight_tiles(initial_state, final_state, heuristic_function):
    g_score = {}
    f_score = {}
    open_set = []

    start_key = tuple(tuple(row) for row in initial_state)
    final_key = tuple(tuple(row) for row in final_state)

    g_score[start_key] = 0
    f_score[start_key] = heuristic_function(initial_state, final_state)
    came_from = {}
    heapq.heappush(open_set, (f_score[start_key], initial_state))

    explored_states = set()


    while open_set:
        _, current = heapq.heappop(open_set)
        current_key = tuple(tuple(row) for row in current)

        if current_key == final_key:
            break

        explored_states.add(current_key)


        next_states = get_neighbors(current)

        for ns in next_states:
            ns_key = tuple(tuple(row) for row in ns)
            new_g_score = g_score[current_key] + 1
            if ns_key not in explored_states or new_g_score < g_score.get(ns_key, float('inf')):
                came_from[ns_key] = current_key

                g_score[ns_key] = new_g_score
                f_score[ns_key] = new_g_score + heuristic_function(ns, final_state)
                new_f_score = f_score[ns_key]
                heapq.heappush(open_set, (new_f_score, ns))

    path = []
    node = final_key
    while node in came_from:
        path.append(node)
        node = came_from[node]
    path.append(start_key)
    path.reverse()
    return path



final_state = [[1,2,3],[4,5,6],[7,8,0]]
initial_state = [[7,2,4],[5,0,6], [8,3,1]]

path = eight_tiles(initial_state, final_state, manhattan_distance)
for index, step in enumerate(path):
    print(f"Step {index}:")
    for row in step:
        print(row)
    print("---")
