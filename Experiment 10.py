import heapq

# Graph as adjacency list: node: [(neighbor, cost), ...]
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 1), ('D', 3)],
    'C': [('A', 4), ('B', 1)],
    'D': [('B', 3)]
}

# Heuristic values (estimated cost to goal 'D')
heuristic = {
    'A': 5,
    'B': 3,
    'C': 6,
    'D': 0
}

def a_star(start, goal):
    queue = []
    heapq.heappush(queue, (0 + heuristic[start], 0, start, [start]))

    while queue:
        f, g, current, path = heapq.heappop(queue)

        if current == goal:
            print("Path found:", path)
            print("Total cost:", g)
            return

        for neighbor, cost in graph[current]:
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(queue, (new_f, new_g, neighbor, path + [neighbor]))

    print("No path found.")

# Example usage
a_star('A', 'D')
