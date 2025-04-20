from collections import deque
import matplotlib.pyplot as plt
import time

def bfs(maze, start, goal):
    visited = set()
    queue = deque([(start, [])])
    
    plt.figure(figsize=(8, 8))
    
    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) in visited:    
            continue
            
        visited.add((x, y))
        path = path + [(x, y)]
        
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



        
