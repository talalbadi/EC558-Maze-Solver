import numpy as np
import random

def generate_maze(size=(25, 25), p=[0.8, 0.2]):
    """
    Generate a random maze with specified size and probability of empty/blocked cells.
    
    Parameters:
    - size: Tuple (height, width) of the maze
    - p: Probability distribution [p_empty, p_blocked]
    
    Returns:
    - maze: 2D numpy array (0 = empty, 1 = blocked)
    - start_position: (row, col) tuple
    - goal_position: (row, col) tuple
    """
    # Generate initial random maze
    maze = np.random.choice([0, 1], size=size, p=p)
    
    # Get all valid (empty) cells
    valid_points = np.argwhere(maze == 0)
    
    if len(valid_points) < 2:
        # If not enough empty cells, regenerate the maze
        return generate_maze(size, p)
    
    # Choose start and goal positions that are far apart
    min_distance = max(size) // 2  # Require at least half the size as distance
    
    # Try to find well-separated start and goal positions
    attempts = 0
    while attempts < 50:  # Limit attempts to avoid infinite loops
        start_idx = random.randint(0, len(valid_points) - 1)
        goal_idx = random.randint(0, len(valid_points) - 1)
        
        start_p = tuple(valid_points[start_idx])
        goal_p = tuple(valid_points[goal_idx])
        
        # Calculate Manhattan distance
        distance = abs(start_p[0] - goal_p[0]) + abs(start_p[1] - goal_p[1])
        
        if distance >= min_distance:
            # Make sure the start and goal positions are not blocked
            maze[start_p[0], start_p[1]] = 0
            maze[goal_p[0], goal_p[1]] = 0
            
            # Check if a path exists between start and goal
            visited = set()
            queue = [(start_p, [])]
            path_exists = False
            
            while queue:
                (x, y), _ = queue.pop(0)
                
                if (x, y) in visited:
                    continue
                    
                visited.add((x, y))
                
                if (x, y) == goal_p:
                    path_exists = True
                    break
                    
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < size[0] and 0 <= ny < size[1] and maze[nx, ny] == 0:
                        queue.append(((nx, ny), []))
            
            if path_exists:
                return maze, start_p, goal_p
        
        attempts += 1
    
    # If we failed to find good start/goal positions, regenerate the maze
    # This may create a more solvable maze
    return generate_maze(size, p)