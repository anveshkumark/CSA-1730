from collections import deque

# Each state: (location, A_status, B_status)
# location: 'A' or 'B'
# status: 'Dirty' or 'Clean'

def vacuum_bfs(initial_state):
    queue = deque()
    queue.append((initial_state, []))  # (current state, path taken)
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        location, a_status, b_status = current_state

        # If goal state reached
        if a_status == 'Clean' and b_status == 'Clean':
            print("Goal reached!")
            for step in path + [current_state]:
                print(step)
            return

        if current_state in visited:
            continue
        visited.add(current_state)

        # Generate next possible states

        # 1. Clean if current location is dirty
        if location == 'A' and a_status == 'Dirty':
            next_state = ('A', 'Clean', b_status)
            queue.append((next_state, path + [current_state]))
        elif location == 'B' and b_status == 'Dirty':
            next_state = ('B', a_status, 'Clean')
            queue.append((next_state, path + [current_state]))

        # 2. Move to other location
        if location == 'A':
            next_state = ('B', a_status, b_status)
            queue.append((next_state, path + [current_state]))
        else:
            next_state = ('A', a_status, b_status)
            queue.append((next_state, path + [current_state]))

# Example usage
initial_state = ('A', 'Dirty', 'Dirty')
vacuum_bfs(initial_state)
