from collections import deque

# State: (M_left, C_left, Boat_side)  Boat_side: 1 - left, 0 - right
def is_valid(state):
    m_left, c_left, m_right, c_right = state[0], state[1], 3 - state[0], 3 - state[1]

    if (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0):
        return False

    if (m_left > 0 and m_left < c_left):
        return False

    if (m_right > 0 and m_right < c_right):
        return False

    return True

def bfs():
    start = (3, 3, 1)  # (Missionaries_left, Cannibals_left, Boat_position)
    goal = (0, 0, 0)
    queue = deque()
    queue.append((start, []))
    visited = set()

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]  # possible boat moves

    while queue:
        current, path = queue.popleft()

        if current[:3] == goal:
            path.append(current)
            for step in path:
                print(step)
            return

        if current in visited:
            continue
        visited.add(current)

        for m, c in moves:
            if current[2] == 1:  # boat on left side
                new_state = (current[0]-m, current[1]-c, 0)
            else:  # boat on right side
                new_state = (current[0]+m, current[1]+c, 1)

            if is_valid(new_state):
                queue.append((new_state, path + [current]))

    print("No solution found.")

bfs()
