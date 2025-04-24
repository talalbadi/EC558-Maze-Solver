import numpy as np
import matplotlib.pyplot as plt
from maze_generator import generate_maze
from maze_solver import *
import time
maze,start_p,goal_p=generate_maze()
IDSAstar(maze,(24,0),(0,24),True)

start_time=time.time()
path=dfs(maze,(24,0),(0,24),True)
end_time=time.time()
print(f"Time taken DFS: {end_time-start_time:.4f} ms")

start_time=time.time()
path=bfs(maze,start_p,goal_p,True)
end_time=time.time()
print(f"Time taken BFS: {end_time-start_time:.4f} ms")

start_time=time.time()
#path=astar(maze,start_p,goal_p)
path=dfs(maze,start_p,goal_p,False)
#path=bfs(maze,start_p,goal_p,True)
end_time=time.time()
print(f"Time taken A*: {end_time-start_time:.4f} ms")

start_time=time.time()
path=ucs(maze,start_p,goal_p,False)
end_time=time.time()
print(f"Time taken UCS: {end_time-start_time:.4f} ms")


plt.imshow(maze, cmap='binary')
plt.scatter(start_p[1], start_p[0], color='green', marker='s')

plt.scatter(goal_p[1], goal_p[0], color='red', marker='s')
plt.title(f"Time taken: {end_time-start_time:.4f} ms")
if path:
    plt.plot([p[1] for p in path], [p[0] for p in path], color='blue')
else:
    print("No path found")
plt.show()

