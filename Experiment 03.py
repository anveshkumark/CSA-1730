from collections import deque

def water_jug_bfs(cap_a, cap_b, target):
    visited = set()
    queue = deque()
    queue.append((0, 0))  # both jugs are initially empty

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        print(f"Jug A: {a} liters, Jug B: {b} liters")

        if a == target or b == target:
            print("Goal reached!")
            return

        # All possible next states
        next_states = [
            (cap_a, b),         # fill Jug A
            (a, cap_b),         # fill Jug B
            (0, b),             # empty Jug A
            (a, 0),             # empty Jug B
            (max(0, a - (cap_b - b)), min(cap_b, b + a)),  # pour A -> B
            (min(cap_a, a + b), max(0, b - (cap_a - a)))   # pour B -> A
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

# Example usage
water_jug_bfs(4, 3, 2)
