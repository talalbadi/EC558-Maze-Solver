from collections import deque

def bfs(maze, start, goal):
    viseted=set()
    queue=deque([(start,[])])

    while queue:
        (x,y),path=queue.popleft()

        if (x,y) in viseted:    
            continue

        viseted.add((x,y))
        path.append((x,y))

        if (x,y)==(goal[0],goal[1]): 
            return path
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<len(maze) and 0<=ny<len(maze[0]) and maze[nx][ny]==0:
                queue.append(((nx,ny),path+[(nx,ny)]))
    return None