# Minimax with Alpha-Beta Pruning

def minimax(position, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or is_terminal(position):
        return evaluate(position)
    
    if maximizingPlayer:
        maxEval = float('-inf')
        for child in get_children(position):
            eval = minimax(child, depth-1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # beta cut-off
        return maxEval
    else:
        minEval = float('inf')
        for child in get_children(position):
            eval = minimax(child, depth-1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # alpha cut-off
        return minEval

# Below are dummy functions to simulate a game

def is_terminal(position):
    # Return True if game over (for demo: if depth reached 0)
    return False

def evaluate(position):
    # Dummy evaluation function
    return position

def get_children(position):
    # Dummy children generator (for demo purpose)
    return [position - 1, position - 2]

# Example usage
initial_position = 5
depth = 3
result = minimax(initial_position, depth, float('-inf'), float('inf'), True)
print("Best value:", result)
