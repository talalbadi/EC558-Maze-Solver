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

# def astar(maze, start, goal):
#     visited = set()
#     queue = deque([(start,[],30)])
#     while queue:
#         (x,y),path,cost = queue.popleft()
#         if (x,y) in visited:
#             continue
#         visited.add((x,y))
#         path = path + [(x,y)]   
#         plt.clf()
#         plt.imshow(maze, cmap='binary')
#         plt.scatter(start[1], start[0], color='green', marker='s')
#         plt.scatter(goal[1], goal[0], color='red', marker='s')
#         plt.plot([p[1] for p in path], [p[0] for p in path], color='blue')
#         plt.title(f'A* Step {len(visited)}')
#         plt.pause(0.1)
#         if (x,y) == (goal[0],goal[1]):
#             return path
#         neghbors=[(x+1,y,cost+30),(x-1,y,cost+30),(x,y+1,cost+30),(x,y-1,cost+30)]
#         for nx,ny,nc in neghbors:
#             if 0<=nx<len(maze) and 0<=ny<len(maze[0]) and maze[nx][ny]==0:
#                 estimated_cost =( abs(nx-goal[0]) + abs(ny-goal[1]) +1)*30
#                 nc+=estimated_cost
#         neghbors.sort(key=lambda x:x[2])
#         for nx,ny,nc in neghbors:
#             if (nx,ny) not in visited and 0<=nx<len(maze) and 0<=ny<len(maze[0]) and maze[nx][ny]==0:
#                 new_path=path+[(nx,ny)]
#                 queue.append(((nx,ny),new_path,nc))
             
#     return None

