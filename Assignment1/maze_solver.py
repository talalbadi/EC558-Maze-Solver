from collections import deque
import matplotlib.pyplot as plt
import time

def bfs(maze, start, goal,visulizeSteps):
    visited = set()
    queue = deque([(start, [])])
    
    plt.figure(figsize=(8, 8))
    
    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) in visited:    
            continue
            
        visited.add((x, y))
        path = path + [(x, y)]
        
        if visulizeSteps:
         plt.clf()
         plt.imshow(maze, cmap='binary')
         plt.scatter(start[1], start[0], color='green', marker='s')
         plt.scatter(goal[1], goal[0], color='red', marker='s')
         plt.plot([p[1] for p in path], [p[0] for p in path], color='blue')
         plt.title(f'BFS: Step {len(visited)}')
         plt.pause(0.1) 
        
        if (x, y) == (goal[0], goal[1]): 
            return path
            
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                queue.append(((nx, ny), path))
    return None

def dfs(maze, start, goal,visulizeSteps=False):
    visited = set()
    stack = [(start, [])]
    
    # Create figure for visualization
    plt.figure(figsize=(8, 8))
    
    while stack:
        (x, y), path = stack.pop()
        
        if (x, y) in visited:
            continue
            
        visited.add((x, y))
        path = path + [(x, y)]
        
        if visulizeSteps:
            plt.clf()
            plt.imshow(maze, cmap='binary')
            plt.scatter(start[1], start[0], color='green', marker='s')
            plt.scatter(goal[1], goal[0], color='red', marker='s')
            plt.plot([p[1] for p in path], [p[0] for p in path], color='blue')
            plt.title(f'DFS: Step {len(visited)}')
            plt.pause(0.1)  
        
        if (x, y) == (goal[0], goal[1]):
            return path
            
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                stack.append(((nx, ny), path))
    return path


def astar(maze, start, goal,visulizeSteps=False):
    visited = set()
    queue = deque([(start, [], 0)])

    while queue:
        (x, y), path, cost = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        path = path + [(x, y)]

        if visulizeSteps:
            plt.clf()
            plt.imshow(maze, cmap='binary')
            plt.scatter(start[1], start[0], color='green', marker='s')
            plt.scatter(goal[1], goal[0], color='red', marker='s')
            plt.plot([p[1] for p in path], [p[0] for p in path], color='blue')
            plt.title(f'A* Step {len(visited)}')
            plt.pause(0.1)

        if (x, y) == (goal[0],goal[1]):
            return path

        neighbors = [
            (x + 1, y, cost + 30),
            (x - 1, y, cost + 30),
            (x, y + 1, cost + 30),
            (x, y - 1, cost + 30)
        ]

        for nx, ny, nc in neighbors:
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                estimated_cost = (abs(nx - goal[0]) + abs(ny - goal[1])) * 30
                f_cost = nc + estimated_cost

                if (nx, ny) not in visited:
                    new_path = path + [(nx, ny)]
                    queue.append(((nx, ny), new_path, f_cost))

        queue = deque(sorted(queue, key=lambda x: x[2]))
    
    return path

def ucs(maze, start, goal,visulizeSteps=False):
    visited = set()
    queue = deque([(start, [], 0)])

    while queue:
        (x, y), path, cost = queue.popleft()
        if (x,y) in visited:
            continue
        visited.add((x,y))
        path=path+[(x,y)]   
        if visulizeSteps:
          plt.clf()
          plt.imshow(maze, cmap='binary')
          plt.scatter(start[1], start[0], color='green', marker='s')
          plt.scatter(goal[1], goal[0], color='red', marker='s')
          plt.plot([p[1] for p in path], [p[0] for p in path], color='blue')
          plt.title(f'UCS Step {len(visited)}')
          plt.pause(0.1)  
        
        if (x,y) == (goal[0],goal[1]):
            return path
        
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<len(maze) and 0<=ny<len(maze[0]) and maze[nx][ny]==0:
                new_path=path+[(nx,ny)]
                new_cost=cost+30
                queue.append(((nx,ny),new_path,new_cost))
    return path

def IDSAstar(maze, start, goal, visulizeSteps=False):
    def heuristic(node):
        return (abs(node[0] - goal[0]) + abs(node[1] - goal[1])) * 30
    
    def search(path, g, bound, visited_nodes):
        current = path[-1]
        f = g + heuristic(current)
        
        if f > bound:
            return f, None
        
        if current == goal:
            return -1, path
        
        min_bound = float('inf')
        visited_nodes.add(current)
        
        if visulizeSteps and len(visited_nodes) % 5 == 0:  # Visualize every 5 steps
            plt.clf()
            plt.imshow(maze, cmap='binary')
            plt.scatter(start[1], start[0], color='green', marker='s')
            plt.scatter(goal[1], goal[0], color='red', marker='s')
            plt.plot([p[1] for p in path], [p[0] for p in path], color='blue')
            plt.title(f'IDA* Step {len(visited_nodes)}')
            plt.pause(0.01)
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)
            
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and neighbor not in path:
                path.append(neighbor)
                t, result = search(path, g + 30, bound, visited_nodes)
                
                if t == -1:
                    return -1, result
                
                if t < min_bound:
                    min_bound = t
                    
                path.pop()
        
        return min_bound, None
    
    # Set up visualization
    if visulizeSteps:
        plt.figure(figsize=(8, 8))
    
    # Initial path contains just the start node
    path = [start]
    visited_nodes = set()
    
    # Initial bound is just the heuristic from start to goal
    bound = heuristic(start)
    
    while True:
        t, result = search(path, 0, bound, visited_nodes)
        
        if t == -1:
            return result
        
        if t == float('inf'):
            return None
        
        bound = t

def greedy_best_first_search(maze, start, goal, visulizeSteps=False):
    visited = set()
    # Priority queue ordered by heuristic value only (not path cost)
    queue = deque([(start, [], 0)])
    
    plt.figure(figsize=(8, 8))
    
    while queue:
        (x, y), path, _ = queue.popleft()
        
        if (x, y) in visited:
            continue
            
        visited.add((x, y))
        path = path + [(x, y)]
        
        if visulizeSteps:
            plt.clf()
            plt.imshow(maze, cmap='binary')
            plt.scatter(start[1], start[0], color='green', marker='s')
            plt.scatter(goal[1], goal[0], color='red', marker='s')
            plt.plot([p[1] for p in path], [p[0] for p in path], color='blue')
            plt.title(f'Greedy Best First Search: Step {len(visited)}')
            plt.pause(0.1)
        
        if (x, y) == (goal[0], goal[1]):
            return path
            
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                # Only use heuristic (Manhattan distance) for ordering
                heuristic = abs(nx - goal[0]) + abs(ny - goal[1])
                neighbors.append((nx, ny, heuristic))
        
        # Sort neighbors by heuristic value
        neighbors.sort(key=lambda x: x[2])
        
        # Add neighbors to queue in order of heuristic value
        for nx, ny, h in neighbors:
            if (nx, ny) not in visited:
                queue.append(((nx, ny), path, h))
    
    return None

