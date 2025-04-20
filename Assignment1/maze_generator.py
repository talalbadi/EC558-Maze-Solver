import numpy as np
import random

def generate_maze(size=(25,25),p=[0.8,0.2]):
    maze =np.random.choice([0,1],size=size,p=p)
    valid_points=np.argwhere(maze==0)
    start_p=random.choice(valid_points)
    goal_p=random.choice(valid_points)
    return maze,start_p,goal_p