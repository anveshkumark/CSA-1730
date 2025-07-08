# Regions and neighbors
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW':['Q', 'SA', 'V'],
    'V':  ['SA', 'NSW'],
    'T':  []
}

colors = ['Red', 'Green', 'Blue']

def is_valid(assignment, region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(neighbors):
        return assignment

    unassigned = [region for region in neighbors if region not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_valid(assignment, region, color):
            assignment[region] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[region]  # backtrack

    return None

# Start solving
solution = backtrack({})
if solution:
    print("Solution found:")
    for region in solution:
        print(f"{region}: {solution[region]}")
else:
    print("No solution found.")
