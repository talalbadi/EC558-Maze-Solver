import numpy as np
import matplotlib.pyplot as plt
from maze_generator import generate_maze
from maze_solver import bfs


maze,start_p,goal_p=generate_maze()

path=bfs(maze,start_p,goal_p)



plt.imshow(maze, cmap='binary')
plt.scatter(start_p[1], start_p[0], color='green', marker='s')
plt.scatter(goal_p[1], goal_p[0], color='red', marker='s')
if path:
    plt.plot([p[1] for p in path], [p[0] for p in path], color='blue')
else:
    print("No path found")
plt.show()

